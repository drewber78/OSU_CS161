# Author: Drew Cochran
# Date: 03NOV2021
# Description: Checks functions for debugging

def mean_func(std_list):
    # For loop to run through and calculate the mean of the user inputted ages
    for i in range(len(std_list)):
        mean_age += std_list[i].get_age()
        mean_age = mean_age // len(std_list)
