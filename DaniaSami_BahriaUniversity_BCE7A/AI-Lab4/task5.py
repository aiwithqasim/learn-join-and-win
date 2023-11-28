#DANIA SAMI AI AND MACHINE LEARNING LAB 04 TASK NO 05
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Test the function for N = 6
n = 6
result = fibonacci(n)

# Print the result
print(f"N = 6 is {result}")