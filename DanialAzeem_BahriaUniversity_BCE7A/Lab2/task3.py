def calculate_sum_and_average_of_digits(input_string):
    digit_sum = 0
    digit_count = 0
    for char in input_string:
        if char.isdigit():
            digit_sum += int(char)
            digit_count += 1
    if digit_count > 0:
        average = digit_sum / digit_count
    else:
        average = 0

    return digit_sum, average
input_string = input("Enter a string: ")
sum_of_digits, average_of_digits = calculate_sum_and_average_of_digits(input_string)
print(f"Entered String: {input_string}")
print(f"Sum of digits: {sum_of_digits}")
print(f"Average of digits: {average_of_digits}")