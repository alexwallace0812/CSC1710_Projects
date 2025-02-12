########################################################################
# File Name: lab10c.py
# Programmer: Alex Wallace
# Course: CSC1710 – Section 1
# Date Submitted: November 2, 2023
# Location: /home/students/awallace/csc1710/Lab10/lab10c.py
# Description: This progrom prompmts the user to enter to different
# sentences and calculates with list methods whether or not they
# are anagrams
# Assistance: Paul helped me with some advanced coding tips
# Compile and Execute: Python3 lab10c.py
# Additional files: None
#######################################################################
# Setting up input strings for the sentences
string1 = input("Input a sentence: ")
string2 = input("Input another sentence: ")
# Converting all strings to uppercase
string1up = string1.upper()
string2up = string2.upper()
# Using list comprehension to add individual values to a list
string1list = [i for i in string1up if i.isalpha()]
string2list = [j for j in string2up if j.isalpha()]
# Sort the list
string1list.sort()
string2list.sort()
# Prints the output of the lists
if string1list == string2list:
    print("They are anagrams")
else:
    print("They are not anagrams")

