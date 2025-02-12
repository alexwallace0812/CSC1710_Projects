# Alex Wallace
# CSC1710 Lab2
# 08/29/23
# Purpose of lab: To get user input, calculate certain values, and print the calculated output
# This program will help the user calculate a monthly budget
print("How many hours per week do you work?")
hours = float(input())
print("How much do you make per hour?")
pay = float(input())
print("How much does rent cost?")
rent = float(input())
print("How much do you spend on groceries in a month")
food = float(input())
gross = hours*pay*4
taxes = gross*.8
profit = taxes-rent-food
print("Your gross monthly salary before taxes and benefits is " + str(gross))
print("Your net monthly salary after taxes and benefits is " + str(taxes))
print("After your expenses, you will take home " + str(profit))

