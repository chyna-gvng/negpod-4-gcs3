#!/usr/bin/python3
# python program that:
#   - Prints 'Weird' (If m is even)
#   - Prints 'Not Weird' (If m is odd and in the inclusive range of 2 to 5)
#   - Prints 'Weird' (If m is odd and in the inclusive range of 6 to 20, print Weird)
#   - Prints 'Not Weird' (If m is odd and greater than  20)

# Ask user for input & find rem
m = int(input("Enter Number: "))
mod = m % 2

# Nested if statement for even & odd (other if statements)
if mod == 0:
    print("Weird")
else:
    if m >= 2 and m <= 5:
        print("Not Weird")
    elif m >= 6 and m <= 20:
        print("Weird")
    elif m > 20:
        print("Not Weird")
    else:
        print("Error")