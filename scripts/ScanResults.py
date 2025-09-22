import os
import re
from typing import Dict, Any, Tuple, Optional, Set
from utils import *


class ScanResults:
    """
    Manages a JSON file of 'scan results' keyed by some function IDs,
    each containing attributes like: 'filepath', 'function_name',
    'function_start_line', 'if_statements', 'loop_statements', etc.
    """

    def __init__(self, json_path: str):
        """
        :param json_path: path to the JSON file with scan results
        """
        # Read the JSON file into a dictionary
        self.scan_data: Dict[str, Any] = read_json(json_path)
        # self.scan_data might look like:
        # {
        #   "95": {
        #       "filepath": "/local2/..._stripped_main_14_103.c",
        #       "function_name": "get_double",
        #       "function_start_line": 120,
        #       ...
        #   },
        #   ...
        # }
    def get(self, entry_id:str) -> Union[None, Dict]:
        return self.scan_data.get(entry_id, None)
    
    def find_fun_scan_results(self, label_filepath: str) -> Optional[str]:
        """
        Given a file path like '/path/to/p03366_s021784433_stripped_process_case_14_86.yaml',
        we parse out (filename, problem, solution, function, start_line, end_line) using `parse_filename`.

        Then for each entry in self.scan_data:
          1) We also parse the entry's 'filepath' via parse_filename.
          2) Compare problem + solution from both sides.
          3) Compare function_name with the label's function.
          4) Compare function_start_line with the label's start_line.
        
        If matched, return the entry ID (like "95"). Otherwise, return None.
        """
        # parse_filename returns something like:
        #   ('p03366_s021784433_process_case_14_86', 'p03366', 's021784433', 'process_case', 14, 86)
        label_file_parts = parse_filename(label_filepath)
        # We'll name them explicitly:
        (label_filename,
         label_dataset,
         label_problem,
         label_solution,
         label_func,
         label_start,
         label_end) = label_file_parts

        if not label_filename:
            # parse_filename failed on label_filepath
            return None

        # Now loop over each entry in our JSON data
        for entry_id, entry_val in self.scan_data.items():
            # Extract the function name / start line from the JSON
            entry_func_name = entry_val.get("function_name", None)
            entry_start_line = entry_val.get("function_start_line", None)
            entry_end_line = entry_val.get("function_end_line", None)
            entry_filepath = entry_val.get("filepath", None)

            if not entry_filepath or not entry_func_name or not entry_start_line:
                continue  # missing data, skip

            # Parse the scan result's 'filepath' to get problem/solution info
            entry_file_parts = parse_filename(entry_filepath)
            # e.g. (entry_filename, entry_problem, entry_solution, entry_function, entry_start, entry_end)
            (entry_filename,
             entry_dataset,
             entry_problem,
             entry_solution,
             entry_parsed_func,
             entry_parsed_start,
             entry_parsed_end) = entry_file_parts

            if not entry_filename:
                # parse_filename failed on the entry's filepath
                continue

            # 1) Compare problem
            if entry_problem != label_problem:
                continue
            # 2) Compare solution
            if entry_solution != label_solution:
                continue
            # 3) Compare function
            # We want to see if the label's function == entry_val["function_name"]
            # or if it matches the parsed function from the scan's filepath. 
            # Typically, we said the JSON has "function_name" that should match label_func.
            if entry_func_name != label_func:
                continue
            # 4) Compare start line
            # We said "ignore end_line for now," so let's see if entry_start_line
            # matches label_start. The user wants that check.
            if entry_start_line != label_start:
                continue

            if entry_end_line != label_end:
                continue

            # If all match, we found the correct entry
            return entry_id

        # If no match found
        print(f"Cannot find scan results for label file {label_filename}")
        return None


Span = Tuple[int, int, int]         # (cond_start, body_start, body_end)


class FunScanResults:
    """
    Work with a single-function *scan_results* dictionary.

    The scanner information is normalised into Span tuples:

        tag            : "loop" | "if" | "else"
        cond_start     : first line of the header / condition
        body_start     : first executable line inside the block
        body_end       : last  line of the block

    Rules you specified
    -------------------
    • LOOP
        (min(header_start_line, loop_statement_start_line),
         loop_body_start_line,
         loop_body_end_line)

    • IF-TRUE  branch
        (condition_start_line,
         true_branch_start_line,
         true_branch_end_line)

    • IF-ELSE branch (only if else_branch_start_line != 0)
        (condition_start_line,
         else_branch_start_line,
         else_branch_end_line)
    """

    # ───────────────────────── public API ────────────────────────────── #

    def __init__(self, scan: Dict):
        self.scan = scan
        self._spans: List[Span] = self._build_spans()

    # 1. counts -------------------------------------------------------------
    def count_structures(self) -> Tuple[int, int, int]:
        """
        Return
            ( #loops,
              #ifs_without_else,
              #ifs_with_else )      where “ifs_with_else” counts each else
        """
        loops = sum(tag == "loop" for tag, *_ in self._spans)
        ifs   = sum(tag == "if"   for tag, *_ in self._spans)
        ifs_plus_else = sum(tag in {"if", "else"} for tag, *_ in self._spans)
        return loops, ifs, ifs_plus_else

    # 2. maximum nesting depth --------------------------------------------
    def max_depth(self) -> int:
        events: List[Tuple[int, int]] = []
        for _, _, body_s, body_e in self._spans:
            events.append((body_s, +1))        # enter
            events.append((body_e + 1, -1))    # leave (inclusive span)
        events.sort()

        depth = best = 0
        for _, delta in events:
            depth += delta
            best = max(best, depth)
        return best

    # 3. depth of a single line -------------------------------------------
    def depth_of_line(self, line: int) -> int:
        return sum(body_s <= line <= body_e for _, _, body_s, body_e in self._spans)

    # 4. depth distance ----------------------------------------------------
    def depth_distance(self, src: int, dst: int) -> int:
        """
        Control-Nesting Distance (CND)
        Number of pushes + pops needed to move execution
        from *src* to *dst* (symmetric-difference of their block sets).
        """
        s_set: Set[Span] = {sp for sp in self._spans if sp[1] <= src <= sp[3]}
        d_set: Set[Span] = {sp for sp in self._spans if sp[1] <= dst <= sp[3]}
        return len(s_set.symmetric_difference(d_set))

    # ───────────────────────── ICS ────────────────────────────── #
    def ics(self, line1: int, line2: int) -> int:
        """
        Interposed-Control-Structure count (ICS)

        How many *block headers* a reader’s eye meets when moving from
        line1 to line2 (exclusive of the lower bound, inclusive of the
        upper bound).  The order of the two lines does not matter.

            • for 'loop'  and 'if' spans: header   = cond_start
            • for an 'else' span        : header   = body_start   (the 'else' keyword)

        Returns
        -------
        int
            Number of distinct headers whose header-line lies in
            (min(line1,line2), max(line1,line2)].
        """
        if line1 == line2:
            return 0

        lo, hi = sorted((line1, line2))
        count = 0

        for tag, cond_start, body_start, _ in self._spans:
            header_line = cond_start if tag in ("loop", "if") else body_start
            if lo < header_line <= hi:
                count += 1

        return count
    

    # ───────────────────────── internal helpers ───────────────────────── #

    def _build_spans(self) -> List[Span]:
        spans: List[Span] = []

        # 1. collect every condition_start_line so we can detect "else-if"
        all_if_cond_starts = {
            ifs["condition_start_line"]
            for ifs in self.scan.get("if_statements", [])
        }

        # 2. loops ---------------------------------------------------------
        for lp in self.scan.get("loop_statements", []):
            spans.append((
                "loop",
                min(lp["header_start_line"], lp["loop_statement_start_line"]),
                lp["loop_body_start_line"],
                lp["loop_body_end_line"]
            ))

        # 3. if / else -----------------------------------------------------
        for ifs in self.scan.get("if_statements", []):
            # true-branch span
            spans.append((
                "if",
                ifs["condition_start_line"],
                ifs["true_branch_start_line"],
                ifs["true_branch_end_line"]
            ))

            # else-branch span (only if it is NOT an 'else-if')
            else_start = ifs.get("else_branch_start_line", 0)
            if else_start and else_start not in all_if_cond_starts:
                spans.append((
                    "else",
                    ifs["condition_start_line"],
                    else_start,
                    ifs["else_branch_end_line"]
                ))

        return spans
    
def condition_range(block_scan_results: Dict) -> Tuple[int, int, int]:
    """
    Given a dictionary describing either an if-statement or a loop-statement,
    return (condition_line, start_line, end_line).

    Examples:
        If-statement block:
        {
            "condition_start_line": 127,
            "condition_end_line": 127,
            "true_branch_start_line": 128,
            "true_branch_end_line": 130,
            "else_branch_start_line": 0,
            "else_branch_end_line": 0,
            "condition_str": "(c == EOF)"
        }
        => returns (127, 127, 130)

        Loop-statement block:
        {
            "header_start_line": 125,
            "header_end_line": 125,
            "loop_body_start_line": 127,
            "loop_body_end_line": 146,
            "loop_statement_start_line": 125,
            "loop_statement_end_line": 147,
            "header_str": "(1)"
        }
        => returns (125, 125, 147)
    """
    if "condition_start_line" in block_scan_results:
        # It's an if- (or similar) statement
        cond_line = block_scan_results["condition_start_line"]
        cond_end = block_scan_results.get("condition_end_line", cond_line)
        true_end = block_scan_results.get("true_branch_end_line", 0)
        else_end = block_scan_results.get("else_branch_end_line", 0)
        # The block extends as far as the max of cond_end, true_end, else_end
        end_line = max(cond_end, true_end, else_end) if cond_line else cond_line
        return (cond_line, cond_line, end_line)
    else:
        # It's a loop statement
        header_line = block_scan_results["header_start_line"]
        loop_statement_end = block_scan_results["loop_statement_end_line"]
        return (header_line, header_line, loop_statement_end)


