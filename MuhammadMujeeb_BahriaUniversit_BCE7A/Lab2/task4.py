def difference_between_max_and_min(nums):
    if len(nums) >= 1:
        min_value = min(nums)
        max_value = max(nums)
        difference = max_value - min_value
        print(f"Input: min = {min_value}, max = {max_value}, difference = {difference}")
    else:
        print("Array should have length 1 or more.")

# Sample Run
difference_between_max_and_min([1, 2, 3, 4, 5, 8, 9, 10, 15, 40, 3])
