import json

original_data = {
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

with open('data.json', 'w') as json_file:
    json.dump(original_data, json_file)

with open('data.json', 'r') as json_file:
    json_data = json.load(json_file)

print("Original dictionary:")
print(original_data)
print("Json file to dictionary:")
print(json_data)
