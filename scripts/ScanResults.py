from typing import Any, Dict, Optional, Set, Tuple
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
        #       "filepath": "/../..._stripped_main_14_103.c",
        #       "function_name": "get_double",
        #       "function_start_line": 120,
        #       ...
        #   },
        #   ...
        # }

    def get(self, entry_id: str) -> Union[None, Dict]:
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
        (
            label_filename,
            label_dataset,
            label_problem,
            label_solution,
            label_func,
            label_start,
            label_end,
        ) = label_file_parts

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
            (
                entry_filename,
                entry_dataset,
                entry_problem,
                entry_solution,
                entry_parsed_func,
                entry_parsed_start,
                entry_parsed_end,
            ) = entry_file_parts

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
