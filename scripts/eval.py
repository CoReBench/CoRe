import json
import os
import sys
from typing import Dict, List

from tqdm import tqdm

sys.path.append("..")
from parse_label import *
import argparse
from utils import *
import csv


############################################################
# Redesigned EvaluationCounter class with confusion matrix
# for classification (Yes/No), plus trace metrics.
############################################################
class EvaluationCounter:
    """
    Tracks:
      - Classification confusion matrix for Yes/No (TP, FP, TN, FN)
      - Trace-based metrics for correct 'Yes' answers
    """

    def __init__(self):
        # Confusion‑matrix counts
        self.tp = 0
        self.fp = 0
        self.tn = 0
        self.fn = 0

        # Trace‑level accumulations (only for correct “Yes” answers)
        self.trace_evals_count = 0
        self.precision_sum = 0.0
        self.recall_sum = 0.0  # control‑dep
        self.false_edge_rate_sum = 0.0  # data/implicit dep
        self.missing_nodes_sum = 0.0  # data/implicit dep
        self.correct_trace = 0.0

        # ─── NEW: Source‑level accumulators ───────────────────────────────
        self.sources_evals_count = 0
        self.sources_precision_sum = 0.0
        self.sources_recall_sum = 0.0
        self.sources_f1_sum = 0.0
        self.sources_acc_sum = 0.0

        self.not_parsed_count = 0

    # ------------------------------------------------------------------
    # Classification helpers
    # ------------------------------------------------------------------
    def update_accuracy(self, predicted: bool, groundtruth: bool) -> bool:
        """Update confusion‑matrix counts. Return True if prediction matches."""
        if predicted and groundtruth:
            self.tp += 1
            return True
        elif predicted and not groundtruth:
            self.fp += 1
            return False
        elif not predicted and not groundtruth:
            self.tn += 1
            return True
        else:  # not predicted and groundtruth
            self.fn += 1
            return False

    # ------------------------------------------------------------------
    # Trace aggregation helpers
    # ------------------------------------------------------------------
    # def update_control_dep(self, precision: float, recall: float):
    #     self.trace_evals_count += 1
    #     self.precision_sum += precision
    #     self.recall_sum += recall

    def update_trace(
        self,
        total_edges: int,
        num_false_edges: int,
        missing_nodes: float,
        precision: float,
    ):
        self.trace_evals_count += 1
        self.precision_sum += precision
        self.missing_nodes_sum += missing_nodes
        if total_edges > 0:
            self.false_edge_rate_sum += num_false_edges / total_edges
        if precision == 1:
            self.correct_trace += 1

    # ------------------------------------------------------------------
    # NEW: Source‑list aggregation helpers
    # ------------------------------------------------------------------
    def update_sources(self, precision: float, recall: float, f1: float, acc: float):
        """
        Accumulate metrics for one evaluated *source list*.
        Call this once per problem instance where sources are scored.
        """
        self.sources_evals_count += 1
        self.sources_precision_sum += precision
        self.sources_recall_sum += recall
        self.sources_f1_sum += f1
        self.sources_acc_sum += acc  # 1 or 0

    # ------------------------------------------------------------------
    # Final metrics
    # ------------------------------------------------------------------
    def compute(self) -> Dict[str, float]:
        total = self.tp + self.fp + self.tn + self.fn
        accuracy = (self.tp + self.tn) / total if total else 0.0
        cls_precision = self.tp / (self.tp + self.fp) if (self.tp + self.fp) else 0.0
        cls_recall = self.tp / (self.tp + self.fn) if (self.tp + self.fn) else 0.0
        f1 = (
            2 * cls_precision * cls_recall / (cls_precision + cls_recall)
            if (cls_precision + cls_recall)
            else 0.0
        )

        # Trace aggregates
        avg_p = avg_fe = avg_miss = correct_trace_rate = 0.0
        if self.trace_evals_count:
            avg_p = self.precision_sum / self.trace_evals_count
            # avg_r = self.recall_sum / self.trace_evals_count
            avg_fe = self.false_edge_rate_sum / self.trace_evals_count
            avg_miss = self.missing_nodes_sum / self.trace_evals_count
            correct_trace_rate = self.correct_trace / self.trace_evals_count

        # ─── Source‑list metrics ─────────────────────────────────────────
        avg_src_p = avg_src_r = avg_src_f1 = avg_src_acc = 0.0
        if self.sources_evals_count:
            avg_src_p = self.sources_precision_sum / self.sources_evals_count
            avg_src_r = self.sources_recall_sum / self.sources_evals_count
            avg_src_f1 = self.sources_f1_sum / self.sources_evals_count
            avg_src_acc = self.sources_acc_sum / self.sources_evals_count
            return {
                "total": self.sources_evals_count,
                "accuracy": avg_src_acc,
                "precision": avg_src_p,
                "recall": avg_src_r,
                "f1": avg_src_f1,
                "avg_trace_precision": avg_p,
                # "avg_trace_recall": avg_r,
                "avg_false_edge_rate": avg_fe,
                "avg_missing_nodes": avg_miss,
                "correct_trace_rate": correct_trace_rate,
            }

        return {
            "total": total,
            "accuracy": accuracy,
            "precision": cls_precision,
            "recall": cls_recall,
            "f1": f1,
            "avg_trace_precision": avg_p,
            # "avg_trace_recall": avg_r,
            "avg_false_edge_rate": avg_fe,
            "avg_missing_nodes": avg_miss,
            "correct_trace_rate": correct_trace_rate,
        }


############################################################
# Main Evaluator class
############################################################
class Evaluator:

    def __init__(
        self,
        response_file: str,
        label_root: str,
        out_root: str,
        trace: bool = False,
        source: bool = False,
    ):
        self.response_file = response_file  # a jsonl
        self.label_root = label_root
        self.out_root = out_root
        self.eval_file = os.path.join(
            out_root, os.path.basename(response_file).replace(".jsonl", "_eval.jsonl")
        )
        self.counter = EvaluationCounter()
        self.not_parsed_count = 0
        self.trace = trace
        self.source = source

    def preprocess_trace(
        self,
        task_type: str,
        trace: List,
        start: int,
        clip: bool,
        list_all: bool = False,
    ) -> List:
        def unpack(node):
            if task_type == "data":
                var, line = node
            else:
                var, line, _ = node
            return [var, line_before_clip(line, start)] if clip else [var, line]

        if list_all:
            if task_type == "control":
                return [line_before_clip(l, start) for l in trace] if clip else trace
            else:
                if not clip:
                    return trace
                ret = []
                for var, line in trace:
                    ret.append([var, line_before_clip(line, start)])
                return ret

        if task_type == "control":
            return [line_before_clip(l, start) for l in trace] if clip else trace

        elif task_type in ("data", "infoflow"):
            path = []
            for entry in trace:
                cur_from = unpack(entry["from"])
                cur_to = unpack(entry["to"])

                if not path:
                    path.append(cur_from)
                elif path[-1] != cur_from:
                    path.append(cur_from)

                path.append(cur_to)

            return path

        else:
            raise ValueError(f"Unsupported task_type: {task_type}")

    def evaluate_trace(
        self, prog, task_type: str, gt_trace: list, candidate_trace: list
    ) -> dict:
        if task_type == "control":
            if len(gt_trace) <= 1:
                gt = gt_trace[0] if gt_trace else []
                return prog.evaluate_control_trace(candidate_trace, verbose=False)
            else:
                best = max(
                    (
                        prog.evaluate_control_trace(candidate_trace, verbose=False)
                        for gt in gt_trace
                    ),
                    key=lambda r: r.get("correct_edges", 0),
                )
                return best

        elif task_type == "data":
            processed_candidate_trace = prog.process_candidate_trace(candidate_trace)
            return prog.evaluate_data_trace(processed_candidate_trace, verbose=False)

        elif task_type == "infoflow":
            processed_candidate_trace = prog.process_candidate_trace(candidate_trace)
            return prog.evaluate_implicit_trace(
                processed_candidate_trace, verbose=False
            )

        else:
            raise ValueError(f"Unsupported task type: {task_type}")

    def evaluate_sources(
        self, prog, task_type: str, candidate_sources: list, target_var: "Variable"
    ) -> dict:
        """
        Evaluate *source–only* predictions.

        Args
        ----
        prog              : Program     – instance with target_var set.
        task_type         : str         – "control", "data", or "infoflow".
        candidate_sources : list        – prediction list
                                        • control : [int, ...]                (lines)
                                        • data    : [(var, line), ...]
                                        • infoflow: [(var, line), ...]

        Returns
        -------
        Dict with precision / recall / f1 (and ground‑truth list from Program).
        """
        if task_type == "control":
            # list[int]
            return prog.evaluate_control_sources(
                target_var, candidate_sources, include_self=True  # prediction
            )

        elif task_type == "data":
            # list[Tuple[str,int]]
            return prog.evaluate_data_sources(
                target_var, candidate_sources, include_self=True
            )

        elif task_type == "infoflow":
            # list[Tuple[str,int]]
            return prog.evaluate_implicit_sources(
                target_var, candidate_sources, include_self=True
            )

        else:
            raise ValueError(f"Unsupported task type: {task_type}")

    def eval_prep(self):
        with open(self.response_file, "r") as f, open(self.eval_file, "w") as out_f:
            for i, line in tqdm(enumerate(f), "Trace prep"):
                try:
                    data = json.loads(line)
                except:
                    print(f"Fail to read line {i+1} for file {self.response_file}")
                    assert False
                task_type = data["task_id"].split("_")[0]
                start = data["start"]
                clip = False  # data["setting"]['clip']
                gt_trace = data.get("groundtruth_trace", [])
                parsed = data["response"]["parsed"]

                if parsed is None:
                    self.not_parsed_count += 1

                if self.source:
                    prog = Program(
                        os.path.join(
                            self.label_root,
                            data["language"],
                            "label",
                            data["label_file"],
                        )
                    )
                    if isinstance(data["dst"], list):
                        target_var = prog.get_variable(data["dst"][0], data["dst"][1])
                    else:
                        target_var = prog.get_variable(linenum=data["dst"])
                    if not target_var:
                        assert False, f"Target variable {data['dst']} not found."
                    processed_list = self.preprocess_trace(
                        task_type,
                        parsed.get("sources", []) if parsed else [],
                        start,
                        clip,
                        list_all=True,
                    )
                    data["response"]["eval"] = self.evaluate_sources(
                        prog, task_type, processed_list, target_var
                    )

                else:
                    # Evaluate answer corectness
                    answer = parsed["answer"] if parsed else False
                    gt = data["groundtruth"]
                    data["response"].setdefault("eval", {})["correct"] = gt == answer

                    # Evaluate trace
                    if self.trace:
                        prog = Program(
                            os.path.join(
                                self.label_root,
                                data["language"],
                                "label",
                                data["label_file"],
                            )
                        )

                        if prog is None or parsed is None:
                            processed_trace = []
                        else:
                            processed_trace = self.preprocess_trace(
                                task_type, parsed["trace"], start, clip
                            )
                        eval_result = self.evaluate_trace(
                            prog, task_type, gt_trace, processed_trace
                        )
                        eval_result["processed_trace"] = processed_trace

                        data["response"]["eval"].update(eval_result)

                json.dump(data, out_f)
                out_f.write("\n")

    def eval(self, lite: Optional[str] = None, reeval: bool = False):
        needs_eval_prep = True
        if os.path.exists(self.eval_file) and not reeval:
            with open(self.eval_file, "r") as ef, open(self.response_file, "r") as rf:
                eval_lines = sum(1 for _ in ef)
                response_lines = sum(1 for _ in rf)
                if eval_lines == response_lines:
                    needs_eval_prep = False

        if needs_eval_prep:
            self.eval_prep()

        if lite:
            lite_metadata = read_json(lite)

        with open(self.eval_file, "r") as f:
            for line in tqdm(f, "Final Eval"):
                data = json.loads(line)
                task_id = data.get("task_id")
                task_type = task_id.split("_")[0]
                language = data["language"]
                if lite and task_id not in lite_metadata[task_type][language]:
                    continue

                if self.source:
                    self.counter.update_sources(
                        data["response"]["eval"]["precision"],
                        data["response"]["eval"]["recall"],
                        data["response"]["eval"]["f1"],
                        data["response"]["eval"]["accuracy"],
                    )

                else:
                    # if data['property']['fun_loc'] < 41:
                    #     continue
                    task_type = task_id.split("_")[0]
                    gt = data["groundtruth"]
                    answer = (
                        data["response"]["parsed"]["answer"]
                        if data["response"]["parsed"]
                        else False
                    )

                    self.counter.update_accuracy(answer, gt)

                    if not self.trace or gt is not True:
                        continue

                    eval = data["response"]["eval"]
                    self.counter.update_trace(
                        eval["total_edges"],
                        eval["num_false_edges"],
                        eval["missing_nodes"],
                        eval["precision"],
                    )

        self.summarize()

    def summarize(self):
        results = self.counter.compute()
        print("\n===== Evaluation Summary =====")
        print(f"Accuracy: {results['accuracy']:.4f}")
        print(f"Precision: {results['precision']:.4f}")
        print(f"Recall: {results['recall']:.4f}")
        print(f"F1: {results['f1']:.4f}")

        if self.counter.trace_evals_count:
            print("\n-- Trace Evaluation Metrics --")
            print(f"Avg Trace Precision: {results['avg_trace_precision']:.4f}")
            print(f"Avg False Edge Rate: {results['avg_false_edge_rate']:.4f}")
            print(f"Avg Missing Nodes: {results['avg_missing_nodes']:.4f}")

        print(f"\nUnparsed Data Points: {self.not_parsed_count}")


def get_setting(filepath):
    if "trace" in filepath:
        trace, source = True, False
    elif "source" in filepath:
        trace, source = False, True
    return trace, source


def evaluate_folder(
    response_folder: str,
    label_root: str,
    out_root: str,
    csv_path: Optional[str] = None,
    lite: Optional[str] = None,
    reeval: bool = False,
):
    os.makedirs(out_root, exist_ok=True)
    results = []
    for fname in sorted(os.listdir(response_folder)):
        if fname.endswith(".jsonl"):
            response_path = os.path.join(response_folder, fname)
            trace, source = get_setting(response_path)
            evaluator = Evaluator(response_path, label_root, out_root, trace, source)
            evaluator.eval(lite, reeval)
            result = {"file": fname.split(".")[0], **evaluator.counter.compute()}
            for k, v in result.items():
                if k in {
                    "accuracy",
                    "precision",
                    "recall",
                    "f1",
                    "avg_trace_precision",
                    "avg_false_edge_rate",
                    "correct_trace_rate",
                }:
                    result[k] = f"{v * 100:.2f}"
                elif isinstance(v, float):
                    result[k] = f"{v:.4f}"
            results.append(result)

    if csv_path:
        with open(csv_path, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=results[0].keys())
            writer.writeheader()
            writer.writerows(results)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Evaluate model predictions.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "-r", "--response_file", type=str, help="Path to response JSONL file."
    )
    group.add_argument(
        "-f",
        "--response_folder",
        type=str,
        help="Path to folder of response JSONL files.",
    )
    parser.add_argument(
        "-l",
        "--label_root",
        type=str,
        required=True,
        help="Path to label root directory (/path/to/CoRe/raw_annotation).",
    )
    parser.add_argument(
        "-o",
        "--out_root",
        type=str,
        required=True,
        help="Directory to store evaluation results.",
    )
    parser.add_argument(
        "-c",
        "--csv",
        type=str,
        help="Optional CSV file path with the summarized results.",
    )
    parser.add_argument(
        "--lite",
        type=str,
        default=None,
        help="Optional path to a lite JSON file specifying a subset of task IDs to evaluate.",
    )
    parser.add_argument(
        "--reeval",
        action="store_true",
        help="re-evaluate and ignore the previous eval.jsonl",
    )

    args = parser.parse_args()

    os.makedirs(args.out_root, exist_ok=True)

    if args.response_file:
        trace, source = get_setting(args.response_file)
        evaluator = Evaluator(
            args.response_file, args.label_root, args.out_root, trace, source
        )
        evaluator.eval(lite=args.lite, reeval=args.reeval)
    else:
        evaluate_folder(
            args.response_folder,
            args.label_root,
            args.out_root,
            args.csv,
            lite=args.lite,
            reeval=args.reeval,
        )
