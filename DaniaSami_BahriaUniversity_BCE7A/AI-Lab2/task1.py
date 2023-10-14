#DANIA SAMI AI AND MACHINE LEARNING LAB 02 TASK NO 01
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

if 13 <= num1 <= 19:
    num1 = 0
if 13 <= num2 <= 19:
    num2 = 0
if 13 <= num3 <= 19:
    num3 = 0

result = num1 + num2 + num3
print(f"First integer : {num1}")
print(f"Second integer : {num2}")
print(f"Third integer : {num3}")
print(f"Sum of integers: {result}")