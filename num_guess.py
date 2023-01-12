# Author: Drew Cochran
# Date: 10/12/2021
# Description: Asks user to play a game. User input inputs an integer, then asks for the user to guess the inputted
#           integer. Once the number is guessed, the program displays the number of guesses it took the user.

# Asks user to input integer to guess
num_guess = int(input("Enter the integer for the player to guess."))

# Asks user for first guess and establishes counter
player_guess = int(input("Enter your guess.\n"))
player_count = 1

# Creating while loop to determine exit conditions
while num_guess != player_guess:
    if player_guess < num_guess:
        player_guess = int(input("Too low - try again:\n"))
    elif player_guess > num_guess:
        player_guess = int(input("Too high - try again:\n"))
    player_count += 1

# Displays number of guesses it took for player to guess integer
if player_count == 1:
    print("You guessed it in", player_count, "try.")
else:
    print("You guessed it in", player_count, "tries.")