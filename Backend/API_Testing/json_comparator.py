#   _   _   _   _   _   _   _   _   _   _  
#  / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ 
# ( H | o | u | s | i | n | g | 2 | . | 0 )
#  \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ 
#

# Author: Daniel 
#
# Description:


import json

def load_json(file_path):
    """Load JSON data from a file."""
    with open(file_path, 'r') as file:
        return json.load(file)

def compare_json(file1, file2):
    """Compare two JSON files and return the differences."""
    json1 = load_json(file1)
    json2 = load_json(file2)

    differences = {}

    # Check for keys in json1 not in json2 or with different values
    for key in json1:
        if key not in json2:
            differences[key] = f"Only in {file1}"
        elif json1[key] != json2[key]:
            differences[key] = f"Different values: {json1[key]} (in {file1}) vs {json2[key]} (in {file2})"

    # Check for keys in json2 not in json1
    for key in json2:
        if key not in json1:
            differences[key] = f"Only in {file2}"

    return differences

def compare_dictionaries(dict1, dict2):
    """Iteratively compare two dictionaries."""
    differences = {}
    stack = [("", dict1, dict2)]

    while stack:
        path, current_dict1, current_dict2 = stack.pop()

        for key in current_dict1:
            if key not in current_dict2:
                differences[path + key] = "Only in first"
            else:
                if isinstance(current_dict1[key], dict) and isinstance(current_dict2[key], dict):
                    stack.append((path + key + ".", current_dict1[key], current_dict2[key]))
                elif current_dict1[key] != current_dict2[key]:
                    differences[path + key] = f"Different values: {current_dict1[key]} (in first) vs {current_dict2[key]} (in second)"

        for key in current_dict2:
            if key not in current_dict1:
                differences[path + key] = "Only in second"

    return differences