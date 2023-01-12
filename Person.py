# Author: Drew Cochran
# Date: 03NOV2021
# Description: Program what takes in user inputted list of people and ages as private data members as parameters,
#           and stores for use in another function to calculate the standard deviation of a groups ages.


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