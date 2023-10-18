import json

original_dict = {
    'students': [
        {'firstName': 'Nikki', 'lastName': 'Roysden'},
        {'firstName': 'Mervin', 'lastName': 'Friedland'},
        {'firstName': 'Aron ', 'lastName': 'Wilkins'}
    ],
    'teachers': [
        {'firstName': 'Amberly', 'lastName': 'Calico'},
        {'firstName': 'Regine', 'lastName': 'Agtarap'}
    ]
}

json_file_path = 'data.json'

with open(json_file_path, 'w') as json_file:
    json.dump(original_dict, json_file, indent=4)

print(f"Original dictionary:\n{original_dict}")
print(f"Json file to dictionary:\n{json.dumps(original_dict, indent=4)}")