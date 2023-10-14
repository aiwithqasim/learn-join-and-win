#DANIA SAMI AI AND MACHINE LEARNING LAB 02 TASK NO 04
def largest_and_smallest_difference(values):
    if len(numbers) < 1:
        return 0

    smallest = min(values)
    largest = max(values)
    difference = largest - smallest

    return f"Min value: {smallest}, Max Value: {largest}, Difference:{difference}"

numbers = [5, 11, 8, 17, 25]
result =largest_and_smallest_difference(numbers)
print(result)