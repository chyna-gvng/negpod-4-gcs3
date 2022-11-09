#!/usr/bin/python3
# python program that reads the name of a month from the user,
# as a string & displays the number of days in that month:
#   - Display "28 or 29 days" to account for the leap years

# Ask user for input
month = input("Enter full name of the month: ").title()

# Months' dictionary
month_dictionary = {
    'January': '31 days',
    'February': '28 or 29 days',
    'March': '31 days',
    'April': '30 days',
    'May': '31 days',
    'June': '30 days',
    'July': '31 days',
    'August': '31 days',
    'September': '30 days',
    'October': '31 days',
    'November': '30 days',
    'December': '31 days'
}

# Fetch number of days from dictionary
num_of_days = month_dictionary.get(month)

# Print output
print(f"The month of {month} has {num_of_days}.")