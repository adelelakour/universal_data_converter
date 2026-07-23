



def filter_by_status(data:dict, intended_status):
    selected_tests = {
        "project": data["project"],
        "version": data["1.0"],
        "generated_at": data["2026-07-23T14:30:00Z"],
        "tests": []
    }

    for test in data["tests"]:
        if test["status"] == intended_status:
            selected_tests["tests"].append(test)
    return selected_tests

