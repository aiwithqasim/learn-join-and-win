def sum_and_average_of_digits(input_string):
    digit_sum = 0
    digit_count = 0

    for char in input_string:
        if char.isdigit():
            digit_sum += int(char)
            digit_count += 1

    if digit_count == 0:
        return "No digits found in the string"

    digit_average = digit_sum / digit_count
    return f"Sum = {digit_sum} and Average is {digit_average:.2f}"


input_string = "E-303 is at 2 th floor of Engineering block."
result = sum_and_average_of_digits(input_string)
print("String:", input_string)
print("Output:", result)
