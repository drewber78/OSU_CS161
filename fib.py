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
    count = 0

    # run the loop to generate the Fibonacci sequence
    while count != num:

        num_final = num1 + num2
        # update the values
        num1 = num2
        num2 = num_final
        count += 1
    return num1