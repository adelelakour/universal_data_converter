import sys
from pathlib import Path
from parsers import read_json

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

allowed_status = [
    "Passed",
    "Failed"
]

def validate_schema(data:dict):

    if "tests" not in data:
        raise KeyError("Missing 'tests' key")

    if len(data["tests"]) == 0:
        raise ValueError("tests list is empty")

    for index, test in enumerate(data["tests"]):
        for key in required_fields:
            if not key in test:
                raise KeyError(f"missing key {key} in test {index}")

def validate_data_types(data:dict):
    for  index, test in enumerate(data["tests"], start=1):
        #validate id
        if not isinstance(test["id"], int):
            raise TypeError(f"ID in test {index} isn't integer")
        if test["id"] < 0:
            raise ValueError(f"id in test {index} must be non-negative")
        #validate name
        if not isinstance(test["name"], str):
            raise TypeError(f"name in test {index} isn't a string")
        #validate category
        if not isinstance(test["category"], str):
            raise TypeError(f"category in test {index} isn't a string")
        #validate status
        if not isinstance(test["status"], str):
            raise TypeError (f"status in test {index} isn't a string")
        #validate priority
        if not isinstance(test["priority"], str):
            raise TypeError(f"priority in test {index} isn't a string")
        #validate duration
        if not isinstance(test["duration"], (int, float)):
            raise TypeError(f"duration in test {index} must be integer or float")
        if test["duration"] < 0:
            raise ValueError(f"duration in test {index} must be non-negative")
        #validate vehicle
        if not isinstance(test["vehicle"], str):
            raise TypeError(f"vehicle in test {index} isn't a string")
        #validate environment
        if not isinstance(test["environment"], str):
            raise TypeError(f"environment in test {index} isn't a string")
        #validate temperature
        if not isinstance(test["temperature"], (int, float)):
            raise TypeError(f"temperature in test {index} must be integer or float")
        #validate executed_by
        if not isinstance(test["executed_by"], str):
            raise TypeError(f"executed_by in test {index} isn't a string")
        #validate timestamp
        if not isinstance(test["timestamp"], str):
            raise TypeError(f"timestamp in test {index} isn't a string")

def validate_status_field(data:dict):
    for index, test in enumerate(data["tests"]):
        if not test["status"] in allowed_status:
            raise ValueError(f"status value of test {index} is invalid")

