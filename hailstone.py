# Author: Drew Cochran
# Date: 10/19/2021
# Description: A function which takes in a positive integer, determines if it is odd or even, and performs certain
#           mathematical operations to the positive integer until said integer is equal to 1, then returns the
#           number of steps it took to make said integer into 1.

def hailstone(num):
    """
    Function that takes in a positive integer value and calculates it down to "1" using mathematical operations.
    If the number is even, it divides by two and then checks if odd or even. If odd, it multiplies by three and adds
    one to the positive integer. The function performs the even/odd check again, counting each time it has to do the
    check until the calculation equals "1". Then the function returns the number of times it took to bring the original
    positive integer back to one.
    :param num:
    :return count:
    """

    # Establish initial variable
    count = 0

    # Checks if num parameter is "1". If so, returns "0"
    if num == 1:
        print("0")

    # Runs while loop to determine the number of times it takes to make num 1
    else:
        while num != 1:
            if num % 2 == 0:
                num = (num / 2)
            else:
                num = (num * 3) + 1
            count += 1
        return count
