def count_characters(string):
    lowercase_count = 0
    uppercase_count = 0
    digit_count = 0
    special_symbol_count = 0

    for char in string:
        if char.islower():
            lowercase_count += 1
        elif char.isupper():
            uppercase_count += 1
        elif char.isdigit():
            digit_count += 1
        else:
            special_symbol_count += 1

    return lowercase_count, uppercase_count, digit_count, special_symbol_count

input_string = input("Enter a string: ")

lowercase, uppercase, digits, special_symbols = count_characters(input_string)

print(f"String: {input_string}")
print(f"Lowercase letters count: {lowercase}")
print(f"Uppercase letters count: {uppercase}")
print(f"Digits count: {digits}")
print(f"Special symbols count: {special_symbols}")