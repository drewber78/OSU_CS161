# Author: Drew Cochran
# Date: 16NOV2021
# Description: Function that takes in two strings and returns a set with the words from both strings.


def words_in_both(string_1, string_2):
    """
    Takes in two strings, splits each string into a list of strings, then compares the two strings to determine which
    words are in both strings, returning that list of words.
    :param string_1:
    :param string_2:
    :return list_set:
    """

    # Establish list_set as a set
    # list_set = {}

    # Create lower each string set into lower case
    split_string_1 = string_1.lower()
    split_string_2 = string_2.lower()

    # Make string parameters into split lists
    split_string_1 = set(split_string_1.split())
    split_string_2 = set(split_string_2.split())

    # Set Intersection to return the result
    # list_set = {split_string_1 & split_string_2}
    return split_string_2 & split_string_1
    # return list_set

test_1 = "Hello my honey."
test_2 = "Hello world."

words_in_both(test_1, test_2)