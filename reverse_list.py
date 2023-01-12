# Author: Drew Cochran
# Date: 07NOV21
# Description: Function that takes in a list as a parameter and reverses the values so the last becomes first, second to last
#           becomes second, etc.


def reverse_list(reversed_list):
    """
    Function that takes in a list and reverses the values from last to first, 2nd to last to 2nd, etc. Does not return anything.
    :param reversed_list:
    :return:
    """

# Creates a deep copy of the list
    copied_list = list(reversed_list)

# Changes first value of reversed_list with the last value of copied list
   # reversed_list[0] = copied_list[(len(reversed_list) - 1)]

# Creates for loop to iterate through the copied list to replace the values in the original reversed_list variable
    for index in range(len(reversed_list)):
            reversed_list[index] = copied_list[-(index + 1)]