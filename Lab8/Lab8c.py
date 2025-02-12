######################################################################## 
# File Name: Lab8c.py
# Programmer: Alex Wallace
# Course: CSC1710 – Section 1
# Date Submitted: October 24, 2023
# Location: /home/students/sstanley/csc1710/Lab8/Lab8c.py
# Description: This program prompts the user to enter multiple names 
# into a list and the program randomly selects winners and removes all
# instances from the list
# Assistance: Paul helped me with the earlier parts of the lab
# Compile and Execute: Python3 Lab8c.py
# Additional files: None
#######################################################################
# Setting up important liness in the program
import random
print("*** Raffle ***")
print("\n")
raffle = []
cycle = ""
# While loop to add names to the raffle
while cycle != "done":
    cycle = input("Enter a ticket name: ")
    if cycle == "done":
        break
    raffle.append(cycle)
# Calculating number of tickets and profits
numtick = len(raffle)
collections = numtick*5
profit = collections-175
# Selecting the winners
thirdwinner = random.choice(raffle)
while thirdwinner in raffle:
    raffle.remove(thirdwinner)
secondwinner = random.choice(raffle)
while secondwinner in raffle:
    raffle.remove(secondwinner)
firstwinner = random.choice(raffle)
while firstwinner in raffle:
    raffle.remove(firstwinner)
# Printing out the results
print("\n")
print(f"First prize goes to {firstwinner}.")
print(f"Second prize goes to {secondwinner}.")
print(f"Third prize goes to {thirdwinner}.")
print(f"We sold {numtick} tickets.")
print(f"We collected ${collections}.")
print(f"Profit: {profit}")
