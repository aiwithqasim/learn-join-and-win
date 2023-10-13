a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if 13 <= a <= 19:
    a = 0
if 13 <= b <= 19:
    b = 0
if 13 <= c <= 19:
    c = 0

result = a + b + c
print(f"First number : {a}")
print(f"Second number : {b}")
print(f"Third number : {c}")
print(f"Sum of entered numbers: {result}")