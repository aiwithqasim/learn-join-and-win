def difference_between_max_and_min(arr):
    if len(arr) < 1:
        return "Array should have at least one element"

    min_val = min(arr)
    max_val = max(arr)

    difference = max_val - min_val

    return f"min = {min_val}, max = {max_val}, difference = {difference}"


input_array = [1, 2, 3, 4, 5, 8, 9, 10, 15, 40, 3]
result = difference_between_max_and_min(input_array)
print("Input:", input_array)
print("Output:", result)
