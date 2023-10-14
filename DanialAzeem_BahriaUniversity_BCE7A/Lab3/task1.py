no_ofrows = 5

for i in range(no_ofrows):
    for j in range(i + 1):
        print("*", end=" ")
    print()

for i in range(no_ofrows - 1, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()