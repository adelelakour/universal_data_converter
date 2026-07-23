import json



def read_json_input(input_file_name):
    with open (input_file_name, 'r') as file:
        data = json.load(file)
    return data

