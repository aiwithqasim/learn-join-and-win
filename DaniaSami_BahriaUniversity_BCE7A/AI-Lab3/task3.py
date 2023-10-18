#DANIA SAMI AI AND MACHINE LEARNING LAB 03 TASK NO 03
month_with_days = {
    'January': 31,
    'February': (28,29),
    'March': 31,
    'April': 30,
    'May': 31,
    'June': 30,
    'July': 31,
    'August': 31,
    'September': 30,
    'October': 31,
    'November': 30,
    'December': 31
}

month = input("Enter the month: ")

month = month.strip().title()

print(f"List of months: January, February, March, April, May, June, July, August, September, October, November, December")
print(f"Input the name of the month: {month}")

if month in month_with_days:
    days = month_with_days[month]
    print(f"No. of days: {days} days.")
else:
    print("Invalid month name. Please enter a valid month name.")