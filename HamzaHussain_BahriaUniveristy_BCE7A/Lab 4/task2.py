import json

original_dict = {
    'students': [
        {'firstName': 'Nikki', 'lastName': 'Roysden'},
        {'firstName': 'Mervin', 'lastName': 'Friedland'},
        {'firstName': 'Aron', 'lastName': 'Wilkins'}
    ],
    'teachers': [
        {'firstName': 'Amberly', 'lastName': 'Calico'},
        {'firstName': 'Regine', 'lastName': 'Agtarap'}
    ]
}

json_data = json.dumps(original_dict, indent=4)

with open('data.json', 'w') as json_file:
    json_file.write(json_data)

with open('data.json', 'r') as json_file:
    loaded_dict = json.load(json_file)

print("Original dictionary:")
print(original_dict)
print("Json file to dictionary:")
print(loaded_dict)
