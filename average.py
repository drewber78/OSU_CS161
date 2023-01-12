# Author: Drew Cochran
# Date: 10/02/2021
# Description: Asks the user for 5 numbers, takes the sum of those numbers, and outputs the average

# Asks for user input and assigns to variables
print("Please enter five numbers.")
user_number = float(input())
user_number += float(input())
user_number += float(input())
user_number += float(input())
user_number += float(input())

avg_number = user_number / 5
# round_decimals

print("The average of those numbers is: ", avg_number, sep="\n")

