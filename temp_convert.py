# Author: Drew Cochran
# Date: 10/02/2021
# Description: Asks the user for a temperature in Celcius and returns the converted
#               temperature in Fahrenheit

# Asks for Celcius input

print("Please enter a Celsius temperature.")
celcius = float(input())

# Converts to Fahrenheit
fahrenheit = ((9/5) * celcius) + 32

# Displays result of conversion

print("The equivalent Fahrenheit temperature is:", fahrenheit, sep="\n")