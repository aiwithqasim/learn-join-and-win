original_list = [
    {'id': '#FF0000', 'color': 'Red'},
    {'id': '#800000', 'color': 'Maroon'},
    {'id': '#FFFF00', 'color': 'Yellow'},
    {'id': '#808000', 'color': 'Olive'}
]

dict_to_remove = {'id': '#FF0000', 'color': 'Red'}

new_list = [d for d in original_list if d != dict_to_remove]

print("Original list of dictionary:")
print(original_list)
print("Remove id #FF0000 from the said list of dictionary:")
print(new_list)
