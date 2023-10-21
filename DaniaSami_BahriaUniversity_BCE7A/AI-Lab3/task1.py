#DANIA SAMI AI AND MACHINE LEARNING LAB 03 TASK NO 01
rows_value = 5

for i in range(rows_value):
    for j in range(i + 1):
        print("*", end=" ")
    print()

for i in range(rows_value - 1, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()