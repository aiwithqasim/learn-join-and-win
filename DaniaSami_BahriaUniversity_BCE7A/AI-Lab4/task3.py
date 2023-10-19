#DANIA SAMI AI AND MACHINE LEARNING LAB 04 TASK NO 03
original_list_dictionary = [
    {'id': '#FF0000', 'color': 'Red'},
    {'id': '#800000', 'color': 'Maroon'},
    {'id': '#FFFF00', 'color': 'Yellow'},
    {'id': '#808000', 'color': 'Olive'}
]

id_removed = {'id': '#FF0000', 'color': 'Red'}

new_list = [d for d in original_list_dictionary if d != id_removed]

print("Original list of dictionaries:")
for d in original_list_dictionary:
    print(d)

print("\nRemove id #FF0000 from the list:")
for d in new_list:
    print(d)