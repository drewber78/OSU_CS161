# Author: Drew Cochran
# Date 02NOV2021
# Description: A function that finds the median from a list of numbers provided by the user through a variable.


def find_median(num_list):
    """
    Function that takes in a user specified variable with an undetermined number of integers and finds the median.
    :param num_list:
    :return:
    """

    # converts and sorts the list
    # int(num_list)
    num_list.sort()

    # If else function to determine if the list elements are odd or even in numbered amount
    if len(num_list) % 2 == 0:
        middle_one = len(num_list) // 2
        middle_two = middle_one - 1
        total = (num_list[middle_one] + num_list[middle_two]) / 2
        return total
    else:
        median = (len(num_list) - 1) // 2
        return num_list[median]
