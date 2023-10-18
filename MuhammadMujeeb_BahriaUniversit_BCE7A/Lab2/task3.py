def sum_and_average_of_digits(input_string):
    digits = [int(char) for char in input_string if char.isdigit()]
    if digits:
        total = sum(digits)
        average = total / len(digits)
        print(f"Sum = {total} and Average is {average}")
    else:
        print("No digits found in the string.")

# Sample Run
sum_and_average_of_digits("Q-301 is at 4 th floor of quaid block.")
