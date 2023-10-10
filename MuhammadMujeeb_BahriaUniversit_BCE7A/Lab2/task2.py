def count_characters(input_string):
    lowercase_count = sum(1 for char in input_string if char.islower())
    uppercase_count = sum(1 for char in input_string if char.isupper())
    digit_count = sum(1 for char in input_string if char.isdigit())
    special_count = len(input_string) - lowercase_count - uppercase_count - digit_count

    print(f"lowercase = {lowercase_count}, uppercase = {uppercase_count}, digits = {digit_count}, special symbols = {special_count}")

# Sample Run
count_characters("ABC123@gmail.com")
