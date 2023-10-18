month_to_days = {
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

month_name = input("Input the name of the month: ")

month_name = month_name.strip().title()

print(f"List of months: January, February, March, April, May, June, July, August, September, October, November, December")
print(f"Input the name of the month: {month_name}")

if month_name in month_to_days:
    days = month_to_days[month_name]
    print(f"No. of days: {days} days.")
else:
    print("Invalid month name. Please enter a valid month name.")