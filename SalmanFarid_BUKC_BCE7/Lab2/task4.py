def diff__largest_and_smallest(values):
    if len(values) < 1:
        return 0

    smallest = min(values)
    largest = max(values)

    return largest - smallest

values = [4, 2, 9, 7, 5]
result = diff__largest_and_smallest(values)
print(result)