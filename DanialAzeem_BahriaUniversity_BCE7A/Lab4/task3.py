original_list = [
    {'id': '#FF0000', 'color': 'Red'},
    {'id': '#800000', 'color': 'Maroon'},
    {'id': '#FFFF00', 'color': 'Yellow'},
    {'id': '#808000', 'color': 'Olive'}
]

removed_item = {'id': '#FF0000', 'color': 'Red'}

new_list = [d for d in original_list if d != removed_item]

print("Original list of dictionaries:")
for d in original_list:
    print(d)

print("\nRemove id #FF0000 from the list:")
for d in new_list:
    print(d)