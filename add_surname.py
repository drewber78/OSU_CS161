# Author: Drew Cochran
# Date: 02NOV2021
# Description: A list comprehension function which takes in user inputed first names to the function, filters out all
#           names with do not start with the letter "K", and returns all the "K" letter names with "Kardashian" added
#           to each.

def add_surname(special_K):
    """
    Function that takes in user parameters for first names, finds only the names that starts with 'K', and returns all
    'K' names with the surname 'Kardashian' added.
    :param special_K:
    :return:
    """

    # Creates list comprehension to filter list
    final = [x + " Kardashian" for x in special_K if x[0] == 'K']
    return final
