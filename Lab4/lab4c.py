######################################################################## 
# File Name: Lab4c.py
# Programmer: Alex Wallace
# Course: CSC1710 – Section 1
# Date Submitted: September 19, 2023
# Location: /home/students/awallace/csc1710/Lab4/Lab4c.py
# Description: This program prompts the user to enter the dimensions of a mural they want to paint and calculates the amount of paint needed along with the total cost
# Assistance: Trint Saunders helped me understand spacing between words
# Compile and Execute: Python3 Lab4c.py
# Additional files: None
#######################################################################
height = float(input("Enter the height of the wall: "))
width = float(input("Enter the width of the wall: "))
rad = float(input("Enter the radius of the circle: "))
coverage = int(input("Enter the paint coverage (square feet per gallon): "))
price = float(input("Enter the price for one gallon of paint: "))
arearect = height*width
areacirc = (rad**2)*3.14
areapurp = areacirc*.15
yellowcov = (arearect-areacirc)/coverage
purplecov = areapurp/coverage
whitecov = (areacirc*2)/coverage
costyellow = yellowcov*price
costpurple = purplecov*price
costwhite = whitecov*price
tot = costyellow+costpurple+costwhite
print("Mural Cost Table:")
print(f"{'Color':<12}{'Gal':>6}{'Cost':>9}")
print(f"{'_':_^27}")
print(f"{'Gold':<12}{yellowcov:>6.2f}{costyellow:>9.2f}")
print(f"{'White':<12}{whitecov:>6.2f}{costwhite:>9.2f}")
print(f"{'Purple':<12}{purplecov:>6.2f}{costpurple:>9.2f}")
print(f"{'_':_^27}")
print(f"{'Total:':>18}{tot:>9.2f}")
