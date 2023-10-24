def sum(a,b,c):
    if a == b or b == c or c == a:
        return 0
    else:
        return a + b + c
    
try:
    Number1 = int(input("Enter Number: "))
    Number2 = int(input("Enter Number: "))
    Number3 = int(input("Enter Number: "))
    
    result = sum(Number1,Number2,Number3)
    print("Result: ")

except ValueError:
    print("Invalid Input")