# Author: Drew Cochran
# Date: 10/11/2021
# Description: Asks the user how many integers user wants to check; prompts user to input said
#       said number of integers, then outputs the min and max of the integers inputted in by the user.


# Prompts user for input of a set number of integers
num_integer = int(input("How many integers would you like to enter?"))

# Prompts user for the integers to check for min and max value
print("Please enter", num_integer, "integers.")

# Establish min and max variable and user's first input
num_store = int(input())
max_val = num_store
min_val = num_store


# Loop to prompt user input and check values to store

while num_integer > 1:
    num_store = int(input())
    if num_store >= max_val:
        max_val = num_store
    elif num_store <= min_val:
        min_val = num_store
    num_integer -= 1

# Display min and max values to user
print("min: ", min_val)
print("max: ", max_val)
