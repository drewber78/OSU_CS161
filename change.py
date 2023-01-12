# Author: Drew Cochran
# Date: 10/02/2021
# Description: Asks the user for a value in cents less than one dollar and returns how many
#              what type of coins and how many the user would have


import decimal

# Asks user for the amount of cents and stores data
print("Please enter an amount in cents less than a dollar.")

cents = int(input())

# Process the amount
quarters = int(cents / 25)
# dimes
# nickels
# pennies


# Outputs result

print("Your change will be:", "Q:", quarters, sep="\n")
