def is_divisible_by_5(binary_number):
    decimal_number = int(binary_number, 2)
    return decimal_number % 5 == 0

input_data = "0100,0011,1010,1001,1100,1001"
binary_numbers = input_data.split(',')
result = [binary_number for binary_number in binary_numbers if is_divisible_by_5(binary_number)]
output = ",".join(result)

print(output)
