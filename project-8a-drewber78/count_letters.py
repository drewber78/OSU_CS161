# Author: Drew Cochran
# Date: 16NOV2021
# Description: Function that takes in a string as a parameter and returns a dictionary with the number of letters
#           counted as capital letters. Returns regardless if the string is empty or has no letters.


def count_letters(string):
    """
    Function that returns a dictionary that displays the count of letters in the string provided as a parameter and
    returns the number of letters in the strings as capitals.
    :return dict:
    """

    # Creating an empty dictionary to store values for return
    dictionary = {}

    # Create an alphabet to check against
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


    # Converting string to a set with upper case and comparing with alphabet
    string = string.upper()
    string = [i for i in string if i in alphabet]

    for a in set(string):
        dictionary[a] = string.count(a)
    sorted(dictionary.items(), key=lambda x: (x[1], x[0]))
    return dictionary


heads = "AdeflzciboDERZc113Zce"
count_letters(heads)