#DANIA SAMI AI AND MACHINE LEARNING LAB 02 TASK NO 03
input_string = input("String: ")
digits = [int(char) for char in input_string if char.isdigit()]
digit_sum = sum(digits)
digit_count = len(digits)
average = digit_sum / digit_count if digit_count > 0 else 0
print(f"Sum = {digit_sum} and Average is {average:.0f}") 