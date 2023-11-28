def Area(radius):
    return math.pi * radius**2

try:
        radius = float(input("Enter Radius"))
        if radius < 0:
            print("Enter Valid Nmuber")
        else:
            area = Area(radius)
            print("Your Area is : ", area)
except ValueError:
    print("Enter A Valid Number")