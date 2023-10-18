#DANIA SAMI AI AND MACHINE LEARNING LAB 02 TASK NO 02
input_string = input("String: ") 

counts = {"lowercase": 0, "uppercase": 0, "digits": 0, "special symbols": 0}

for char in input_string:
    if char.islower():
        counts["lowercase"] += 1
    elif char.isupper():
        counts["uppercasel"] += 1
    elif char.isdigit():
        counts["digits"] += 1
    else:
        counts["special symbols"] += 1 

for category, count in counts. items():
    print(f"{category} {count}", end=", ")
    print()