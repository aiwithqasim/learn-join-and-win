original_list = [
    {'id': '#FF0000', 'color': 'Red'},
    {'id': '#800000', 'color': 'Maroon'},
    {'id': '#FFFF00', 'color': 'Yellow'},
    {'id': '#808000', 'color': 'Olive'}
]


remove = '#FF0000'
new_list = [d for d in original_list if d['id'] != remove]

print("Original list of dictionary:")
print(original_list)
print(f"Remove id {remove} from the said list of dictionary:")
print(new_list)
