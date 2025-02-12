########################################################################
# File Name: lab6c.py
# Programmer: Alex Wallace
# Course: CSC1710 – Section 1
# Date Submitted: October 2, 2023
# Location: /home/students/sstanley/csc1710/Lab6/lab6c.py
# Description: This program prompts the user to enter a year and the
# program calculates whether or not the year is a leap year and it has
# some parameters and rules
# Assistance: Dalton helped me with fixing some issues
# Compile and Execute: python3 lab6c.py
# Additional files: None
#######################################################################
# This statement gets input from the user for each year
year = int(input("Enter a year: "))
# This shows that if it's 2023, it shows present tense
if year==2023:
    print("2023 is not a leap year")
# Calculates if it's going to be a leap year and prints the outcome
if year>2023 and year%4==0 and not(year%100==0) or year>2023 and year%400==0:
    print(f"{year} will be a leap year.")
elif year>2023 and not(year%4==0) and year%100==0 or year>2023 and not(year%400==0):
    print(f"{year} will not be a leap year")
if year<2023 and year%4==0 and not(year%100==0) or year<2023 and year%400==0:
    print(f"{year} was a leap year.")
elif year<2023 and not(year%4==0) and year%100==0 or year<2023 and not(year%400==0):
    print(f"{year} was not a leap year.")
