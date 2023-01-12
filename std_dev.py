# Author: Drew Cochran
# Date: 03NOV2021
# Description: Program what takes in user inputted list of people and ages as private data members as parameters,
# #           and stores for use in another function to calculate the standard deviation of a groups ages.
#               A function that takes in a user defined list from the "Person" class and calculates the standard deviation
#               of the inputted ages from the list.


class Person:
    """
    Person object that accepts in the user defined list of names and ages for people to store to calculate the standard
    deviation of ages.
    """

    def __init__(self,name,age):
        """
        Init's the values to store age's and names.
        :param name:
        :param age:
        """

        self._name = name
        self._age = age

    def get_age(self):
        """
        Takes in user request to return the age of a person input by the user
        :return _age:
        """

        return self._age


# Creates function to calculate the standard deviation
def std_dev(std_list):
    """
    Function that takes in a list of names and ages and returns the standard deviation of the ages.
    :param std_list:
    :return age_dev:
    """

    # Establishes global variable age_dev to eliminate PyCharm "unresolved reference" error
    age_dev = 0
    mean_age = 0

    # For loop to run through and calculate the mean of the user inputted ages
    for i in range(len(std_list)):
        mean_age += std_list[i].get_age()

    # Finishes and finds the mean
    mean_age = mean_age / len(std_list)

    # Finding the square of each age value's distance to the mean and summing it all together
    for i in range(len(std_list)):
        age_dev += (std_list[i].get_age() - mean_age) ** 2

    # Finds the standard deviation from the data calculated above and returns it

    return (age_dev / len(std_list)) ** 0.5
