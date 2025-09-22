import os
import yaml
from typing import List, Dict, Union, Any, Tuple
import json
import re
import os


def read_json(file_path: str) -> Any:
    """
    Reads and returns JSON data from the specified file path.

    :param file_path: The path to the JSON file.
    :type file_path: str
    :return: The parsed JSON data (often a dict or list).
    :rtype: Any
    :raises FileNotFoundError: If the file does not exist.
    :raises json.JSONDecodeError: If the file is not valid JSON.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)
    

def read_yaml(file_path):
    """
    Reads a YAML file and returns its contents as a Python dictionary.

    :param file_path: Path to the YAML file.
    :return: Dictionary containing YAML data.
    """
    try:
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
        return data
    except FileNotFoundError:
        print(f"Error: File not found at path {file_path}")
        return None
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file: {e}")
        return None

def get_file_list(dir_addr):

    files = []
    for _,_, filenames in os.walk(dir_addr):
        files.extend(filenames)
        break

    if '.DS_Store' in files:
        files.remove('.DS_Store')

    return files


def read_file(file_path) -> List[str]:
    """Helper function to read the content of a file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

def make_dir_if_not_exist(path: str) -> None:
    """
    Create the directory at the given path (and any parent directories) if it doesn't already exist.
    """
    try:
        os.makedirs(path, exist_ok=True)
    except OSError as e:
        raise RuntimeError(f"Failed to create directory '{path}': {e}")



def line_after_clip(line:int, start:int):
    return line - start + 1

def line_before_clip(line:int, start:int):
    return line + start - 1

class LabelError(Exception):
    def __init__(self, message = ""):
        self.msg = message



def parse_filename(file_path: str) -> Tuple[str, str, str, str, str, int, int]:
    # example input: 'gcj_524_7220_run_horses_5_33.yaml'
    # example output: ('gcj_524_7220_run_horses_5_33', 'gcj', '524', '7220', 'run_horses', 5, 33)

    filename_with_ext = os.path.basename(file_path)
    filename, _ = os.path.splitext(filename_with_ext)
    filename = filename.replace("_stripped", "")

    # Match from the right to extract start and end
    parts = filename.split('_')
    if len(parts) < 6:
        return (None, None, None, None, None, None, None)

    try:
        start_line = int(parts[-2])
        end_line = int(parts[-1])
    except ValueError:
        return (None, None, None, None, None, None, None)

    dataset = parts[0]
    problem = parts[1]
    solution = parts[2]
    function = '_'.join(parts[3:-2])

    return (
        filename,
        dataset,
        problem,
        solution,
        function,
        start_line,
        end_line
    )


def get_file_loc(file_path: str) -> int:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        return len(lines)
    except Exception as e:
        return 0
    