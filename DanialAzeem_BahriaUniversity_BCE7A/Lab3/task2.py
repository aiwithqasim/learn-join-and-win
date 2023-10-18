def is_divisible_by_5(binary_str):
    decimal_no = int(binary_str, 2)
    return decimal_no % 5 == 0

values = input("Enter a sequence of comma-separated 4-digit binary numbers: ")

binary_numbers = values.split(',')

divisible_by_5 = [binary for binary in binary_numbers if is_divisible_by_5(binary.strip())]

result = ', '.join(divisible_by_5)
print(f"Comma-separated 4-digit binary numbers: {values}")
print("Numbers divisible by 5:", result)