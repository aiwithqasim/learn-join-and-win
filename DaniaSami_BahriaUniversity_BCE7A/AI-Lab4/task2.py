#DANIA SAMI AI AND MACHINE LEARNING LAB 04 TASK NO 02
import json

original_dictionary = {
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

# Define the JSON file path
json_file_path = 'dictionary.json'

# Write the dictionary data to a JSON file
with open(json_file_path, 'w') as json_file:
    json.dump(original_dictionary, json_file, indent=4)

print(f"Original dictionary:\n{original_dictionary}")
print(f"Json file to dictionary:\n{json.dumps(original_dictionary, indent=4)}")