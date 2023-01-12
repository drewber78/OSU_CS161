# Author: Drew Cochran
# Date: 10/17/2021
# Description: Takes in a user's specified position in the Fibonacci sequence
#           and returns the value of the sequence to the user.


def fib(num):
    """
    Accepts a user defined position for the Fibonacci sequence,
    checks the sequence for the value in the user specified position,
    and returns the Fibonacci value specified by the position the user requested.
    :param num:
    :return num1:
    """


# establish initial terms
    num1, num2 = 0, 1
# position == num
    #position = int(input("Please enter the number of Fibonacci terms you want to calculate."))

# check if the number of terms is valid
#    if position <= 0:
#        print("Please enter a positive whole number.")

# Return the one term if user enters only one number
#    elif position == 1:
#        print("Fibonacci sequence up to", position, ":")
#        print(position)

# run the loop to generate the Fibonacci sequence
#    else:
    print("Fibonacci sequence:")
    for n in range(0, (num + 1)):
        return num1
        num_final = num1 + num2
        # update the values
        num1 = num2
        num2 = num_final

