# Author: Drew Cochran
# Date 07NOV2021
# Description: Function that takes in a list as a parameter and squares each value in the list. Does not return anything,
#               requires user to print out used variable to determine new values.


def square_list(values_list):
    """
    Performs a for loop to square each value of the inputted list and replaces each value in the inputted list with
    it's square. Does not return.
    :param values_list:
    :return:
    """
# For loop creation to run the length of the list
    for i in range(len(values_list)):
        # Pulls value from list, squares, and replaces old value with squared value
        values_list[i] = values_list[i] ** 2