#!/usr/bin/env python3
import parsers
import validator
import sys
from pathlib import Path


def main():
    input_file_name = sys.argv[1]
    # output_file_name = sys.argv[2]
    INPUT_FILE = Path("input") / input_file_name
    retrieved_data = parsers.read_json_input(INPUT_FILE)

    try:
        validator.validate_json_schema(retrieved_data)
    except KeyError as e:
        print(f"validation failed {e}")



    return True


if __name__ == "__main__":
    main()