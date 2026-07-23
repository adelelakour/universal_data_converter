import json
import csv
import yaml


def read_json(input_file_name):
    with open (input_file_name, 'r') as file:
        data = json.load(file)
    return data


def read_csv(input_file_name):
    with open (input_file_name, 'r') as file:
        tests = list(csv.DictReader(file))
        for test in tests:
            test["duration"] = float(test["duration"])
            test["id"] = int(test["id"])
            test["temperature"] = int(test["temperature"])
    return {
        "project": "Unknown",
        "version": "Unknown",
        "generated_at": None,
        "tests": tests,
    }


def read_yaml(input_file_name):
    with open (input_file_name, 'r') as file:
        data = yaml.safe_load(file)
    return data