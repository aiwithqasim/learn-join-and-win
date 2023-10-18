month_days = {
    "January": 31,
    "February": "28/29 days",
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31,
}

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

month_name = input("Input the name of Month: ")

if month_name in month_days:
    days = month_days[month_name]
    print(f"No. of days: {days}")
else:
    print("Invalid month name. Please enter a valid month name.")


