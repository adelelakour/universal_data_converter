import sys
from pathlib import Path

from parsers import read_json_input

required_fields = [
    "id",
    "name",
    "category",
    "status",
    "priority",
    "duration",
    "vehicle",
    "environment",
    "temperature",
    "executed_by",
    "timestamp"
]

def validate_json_schema(data:dict):

    for key in required_fields:
        for block in data["tests"]:
            if not key in block:
                raise KeyError(f"missing key {key}")

