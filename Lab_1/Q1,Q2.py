#Question 1
print("(He said, “Don’t do this”)")
print(" ")
print(" ")

#Question 2
def add(x,y):
    return x + y
def sub(x,y):
    return x - y
def mul(x,y):
    return x * y
def dele(x,y):
    if y == 0:
        return "Enter number greater than 0"
    return x/y

while True:
    print("You have a Multiple Option.")
    print("For Addition (add)")
    print("For Subtraction (sub)")
    print("For Multiplication (mul)")
    print("For Deletion (dele)")
    
    user_input = input("Now Write: ")
    if user_input == "quit":
        break
    elif user_input in ("add","sub","mul","dele"):
        Number1 = float(input("Enter number: "))
        Number2 = float(input("Enter number: "))
        
        if user_input == "add":
            print("Result: ", add(Number1,Number2))
        elif user_input == "sub":
            print("Result: ", sub(Number1,Number2))
            
        elif user_input == "mul":
            print("Result: ", mul(Number1,Number2))
        elif user_input == "dele":
            print("Result: ", dele(Number1,Number2))
        
        else:
            print("Invalid Input.")

    
    

