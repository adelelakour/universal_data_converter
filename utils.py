import sys
from pathlib import Path


def get_files_from_user():
    input_file_name = sys.argv[1]
    output_file_name = sys.argv[2]
    #file paths
    INPUT_FILE = Path("input") / input_file_name
    OUTPUT_FILE = Path("output") / output_file_name
    return INPUT_FILE, OUTPUT_FILE