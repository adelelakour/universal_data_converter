



def filter_by_passed_test(data:dict):
    passed_tests = {
        "project": "Autonomous Vehicle Validation",
        "version": "1.0",
        "generated_at": "2026-07-23T14:30:00Z",
        "tests": []
    }
    for test in data["tests"]:
        if test["status"] == "Passed":
            passed_tests["tests"].append(test)
    return passed_tests


def filter_by_failed_test(data:dict):
    failed_tests = {
        "project": "Autonomous Vehicle Validation",
        "version": "1.0",
        "generated_at": "2026-07-23T14:30:00Z",
        "tests": []
    }
    for test in data["tests"]:
        if test["status"] == "Failed":
            failed_tests["tests"].append(test)
    return failed_tests

