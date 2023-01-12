# Author: Drew Cochran
# Date: 10/11/2021
# Description: Asks the user for a positive integer, finds all the factors of said integer,
# and displays factors in ascending order

# Asks user to input a positive integer
user_int = int(input("Please enter a positive integer:"))

# Prints response
print("The factors of", user_int, "are:")

# Print factor 1 as every integer has 1 as a factor
# print("1")

# Loop to determine factors of integer entered
for i in range(user_int + 1, 0, -1):
    user_factor = user_int // i
    if user_int % i == 0:
        print(user_factor)
    i += 1