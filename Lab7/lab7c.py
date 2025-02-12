########################################################################
# File Name: labyc.py
# Programmer: Alex Wallace
# Course: CSC1710 – Section 1
# Date Submitted: October 17, 2023
# Location: /home/students/awallace/csc1710/Lab7/lab7c.py
# Description: This program prompts the user if they want to play the
# the dice game, then rolls random dice and calculates whether they win
# or lose from certain conditions
# Assistance: Dalton helped me with fixing some issues
# Compile and Execute: python3 lab7c.py
# Additional files: None
#######################################################################

# Setting up the program and its variables
import random

games = 0
wins = 0
losses = 0
ties = 0

plagain = "y"
# Beginning of the while loop for the game and breaks the loop
while plagain == "y":
    plagain = input("Do you want to play Dice? (y or n)")
    if plagain == "n":
        print("Thanks for playing!")
        break
# increasing num of game and calculating dice rolls
    games = games + 1
    user1 = random.randint(1,6)
    user2 = random.randint(1,6)
    comp1 = random.randint(1,6)
    comp2 = random.randint(1,6)
# print outcomes
    print(f"You rolled a {user1} and {user2}.")
    print(f"The computer rolled a {comp1} and {comp2}.")
# if statements to calculate who wins in each condition
    if user1 == user2 > comp1 == comp2:
        print("You win!")
        wins = wins + 1
    elif user1 == user2 < comp1 == comp2:
        print("You lose!")
        losses = losses + 1
    elif user1 == user2 and comp1 != comp2:
        print("You win!")
        wins = wins + 1
    elif user1 != user2 and comp1 == comp2:
        print("You lose!")
        losses = losses + 1
    elif user1 == user2 == comp1 == comp2:
        print("It's a tie!")
        ties = ties + 1
    elif user1 == comp1 and user2 == comp2 or user1 == comp2 and user2 == comp1:
        print("It's a tie!")
        ties = ties + 1
    elif user1 > (comp1 and comp2) or user2 > (comp1 and comp2):
        print("You win!")
        wins = wins + 1
    else:
        print("You lose!")
        losses = losses + 1
# print stats
    print(f"Games: {games}")
    print(f"Wins: {wins}")
    print(f"Losses: {losses}")
    print(f"Ties: {ties}")
