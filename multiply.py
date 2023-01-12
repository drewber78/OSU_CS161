# Author: Drew Cochran
# Date: 26OCT2021
# Description: Recursive function to multiply two positive integers together and returns the product of those two numbers. Does not use loops
#           and must use addition to figure out the result.

def multiply(num, num2):
    """
       Returns the multiplication of two numbers using recursion and addition.
    :param num:
    :param num2:
    :return:
    """

    if num2 != 1:
        return num + multiply(num, (num2 - 1))
    else:
       return num