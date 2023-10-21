#DANIA SAMI AI AND MACHINE LEARNING LAB 03 TASK NO 02
def divide_by_5(binary_str):
    decimal_no = int(binary_str, 2)
    return decimal_no % 5 == 0

numbers = input("Enter comma-separated 4-digit binary numbers: ")

numbers_in_binary = numbers.split(',')

divisible_by_5 = [binary for binary in numbers_in_binary if divide_by_5(binary.strip())]

result = ', '.join(divisible_by_5)
print(f"Comma-separated 4-digit binary numbers: {numbers}")
print("Binary Numbers divisible by 5:", result)