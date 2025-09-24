import os
import json
import time
from typing import Optional, Dict, Any
from tqdm import tqdm
from parse_response import *
from LLM import *
import argparse
from multiprocessing import Pool, cpu_count
import traceback
import sys
from utils import *

# Constants
MAX_ITER = 3
MAX_PROC = 10
TIMEOUT_ITER = 100
RETRY_PROMPT = (
    "Your previous response could not be parsed correctly. "
    "Please re-read the prompt and ensure your answer strictly follows the required JSON format enclosed with ```<your response here>```."
    "Ensure that your JSON is valid and matches the specification. Try again:"
)


MODEL_MAP = {
    "claude3.5": Claude.V3,
    "claude3.7": Claude.V3_7,
    "claude3.7-thinking": Claude.V3_7_THINKING,
    "llama3-405b": LLAMA.V3_405,
    "ds-r1": DEEPSEEK.R1,
    "ds-v3": DEEPSEEK.V3,
    "gpt-4o": OAI.GPT_4O,
    "o3": OAI.O3,
    "o4-mini": OAI.O4_MINI,
    "qwen3": QWEN.V3_235B,
    "gemini": GEMINI.PRO_2_5
}

def run_inference(prompt_file: str, response_folder: str, model="Claude.V3", max_tokens=500, temperature=0, lite: Optional[str]=None, trace:bool=False) -> None:
    os.makedirs(response_folder, exist_ok=True)

    if lite:
        lite_metadata = read_json(lite)

    if model not in MODEL_MAP:
        print("Invalid model. Current supported models: ", MODEL_MAP.keys())
    llm = LLM(model_id=MODEL_MAP[model], max_token_to_sample=max_tokens, temperature=temperature)

    with open(prompt_file, 'r') as f:
        lines = f.readlines()

    base_filename = os.path.splitext(os.path.basename(prompt_file))[0] + "_response.jsonl"
    output_path = os.path.join(response_folder, base_filename)

    # Read previously processed task_ids
    processed_task_ids = set()
    if os.path.exists(output_path):
        with open(output_path, 'r', encoding='utf-8') as outf:
            for line in outf:
                try:
                    record = json.loads(line)
                    task_id = record.get("task_id")
                    if task_id:
                        processed_task_ids.add(task_id)
                except json.JSONDecodeError:
                    continue  # Optionally log bad lines


    with open(output_path, 'a') as out_f:
        for idx in tqdm(range(len(lines)), desc="Processing prompts"):
            data = json.loads(lines[idx])
            task_id = data.get("task_id")
            task_type = task_id.split('_')[0]
            language = data['language']
            if task_id in processed_task_ids:
                continue
            if lite and task_id not in lite_metadata[task_type][language]:
                continue

            prompt_text = data.get("prompt", "")
            task_id = data["task_id"]
            
            if not prompt_text:
                continue

            messages = [{"role": "user", "content": prompt_text}]
            responses = []
            parsed_result = None
            input_len, output_len = -1, -1
            total_time = -1
            success = False

            for timeout_attempt in range(TIMEOUT_ITER):
                try:
                    start_time = time.time()
                    for _ in range(MAX_ITER):
                        response, in_len, out_len = llm.predict(messages)
                        responses.append(response)
                        parsed_result = parse_dependence_output(response, task_type, trace=trace)
                        if parsed_result is not None:
                            input_len, output_len = in_len, out_len
                            break
                        else:
                            messages.append({"role": "assistant", "content": response})
                            messages.append({"role": "user", "content": RETRY_PROMPT})

                    total_time = time.time() - start_time
                    success = True
                    break
                except Exception as e:
                    print(f"[Error] model failed on {prompt_file} line {idx}: {e}")
                    traceback.print_exc()
                    time.sleep(5)  # optional delay between retries

            if not success:
                print(f"[FATAL] Model consistently failed for {prompt_file} at task {task_id}. Please investigate.")
                break  # pause entire prompt_file


            result_data = dict(data)  # start from original
            result_data['response'] = {
                "original": responses,
                "parsed": parsed_result,
                "input_len": input_len,
                "output_len": output_len,
                "num_iter": len(responses),
                "time": total_time
            }
            json.dump(result_data, out_f)
            out_f.write("\n")

       
def _parallel_worker(args):
    run_inference(*args)

def run_inference_on_folder(prompt_folder: str, response_folder: str,
                             model="Claude.V3", max_tokens=500, temperature=0, lite: Optional[str] = None, trace:bool=False, source:bool=False) -> None:
    tasks = []
    for filename in os.listdir(prompt_folder):
        if filename.endswith(".jsonl"):
            if trace and not ('trace' in filename):
                continue
            if source and not ('source' in filename):
                continue
            prompt_file_path = os.path.join(prompt_folder, filename)
            tasks.append((prompt_file_path, response_folder, model, max_tokens, temperature, lite, trace))

    with Pool(processes=MAX_PROC) as pool:
        list(tqdm(pool.imap_unordered(_parallel_worker, tasks), total=len(tasks), desc="Batch Processing"))

def parse_args():
    parser = argparse.ArgumentParser(description="Run LLM inference on control dependence prompts.")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--prompt_file", type=str, help="Path to the input JSONL file with prompts.")
    group.add_argument("--prompt_folder", type=str, help="Directory containing multiple JSONL prompt files.")

    parser.add_argument("--result_folder", type=str, required=True,
                        help="Root directory where results will be stored under subfolders named by model.")
    parser.add_argument("--model", type=str, default="Claude.V3", help="LLM model identifier. Check LLM.py for supported models.")
    parser.add_argument("--max_tokens", type=int, default=500, help="Max tokens for model to generate.")
    parser.add_argument("--temperature", type=float, default=0, help="Temperature setting for the model.")

    parser.add_argument("--lite", type=str, default=None,
                        help="Optional path to a lite JSON file specifying a subset of task IDs to process.")
    
    parser.add_argument("--trace", action="store_true",
                        help="(Only valid with --prompt_folder) Only run the experiment with trace generation.")

    parser.add_argument("--source", action="store_true",
                        help="(Only valid with --prompt_folder and --lite) Only run the experiment for dependency source generation. Only run with lite")

    args = parser.parse_args()
    if args.trace and not args.prompt_folder:
        print("❌ Error: --trace is only valid when using --prompt_folder.")
        sys.exit(1)
    
    if args.source and not args.prompt_folder and not args.lite:
        print("❌ Error: --source is only valid when using --prompt_folder and --lite")
        sys.exit(1)

    if (not args.source and not args.trace) or (args.source and args.trace):
        print(f"❌ Error: eactly one of --trace and --source need to be set. ")
    # Build output paths
    model_dir = os.path.join(args.result_folder, args.model)
    args.response_folder = os.path.join(model_dir, "response")
    os.makedirs(args.response_folder, exist_ok=True)

    return args



if __name__ == "__main__":
    args = parse_args()

    if args.prompt_file:
        print(f"Running inference on single file: {args.prompt_file}")
        run_inference(
            prompt_file=args.prompt_file,
            response_folder=args.response_folder,
            model=args.model,
            max_tokens=args.max_tokens,
            temperature=args.temperature,
            lite=args.lite,
            trace=args.trace
        )
    else:
        print(f"Running inference on all files in folder: {args.prompt_folder}")
        run_inference_on_folder(
            prompt_folder=args.prompt_folder,
            response_folder=args.response_folder,
            model=args.model,
            max_tokens=args.max_tokens,
            temperature=args.temperature,
            lite=args.lite,
            trace=args.trace,
            source=args.source
        )
