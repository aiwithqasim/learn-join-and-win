def count_characters(input_string):
    lowercase_count = 0
    uppercase_count = 0
    digit_count = 0
    special_symbol_count = 0

    for char in input_string:
        if char.islower():
            lowercase_count += 1
        elif char.isupper():
            uppercase_count += 1
        elif char.isdigit():
            digit_count += 1
        else:
            special_symbol_count += 1

    return lowercase_count, uppercase_count, digit_count, special_symbol_count


input_string = "Hamzee426@gmail.com"
lowercase, uppercase, digits, special_symbols = count_characters(input_string)
print("String:", input_string)
print("Output: lowercase =", lowercase, ", uppercase =", uppercase, ", special symbols =", special_symbols, ", digits =", digits)
