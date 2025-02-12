######################################################################## 
# File Name: Lab5C.py
# Programmer: Alex Wallace
# Course: CSC1710 – Section 1
# Date Submitted: September 19, 2023
# Location: /home/students/sstanley/csc1710/Lab5/lab5c.py
# Description: This program prompts the user to input a number of sales
# to calculate the paycheck that the user will get at the end of the
# month
# Assistance: Dalton helped me with fixing some issues
# Compile and Execute: Python3 lab5c.py
# Additional files: None
#######################################################################

# This first part calculates pay and the bonus
print("*** Welcome to DunderMifflin ***")
sales = int(input("How many sales did you make this month? "))
if sales > 2000 and sales < 4000 or sales == 2000:
    bonus = .06
elif sales > 4000 and sales < 5000 or sales == 4000:
    bonus = .08
elif sales > 5000:
    bonus = .1
# This part is calculating amounts
tax = .15
bonusamt = (bonus*sales)
gross = bonusamt + sales
federaltaxamt = gross*tax
paycheck = gross - federaltaxamt
# This part will print the outcomes
print(f"Your base pay is ${sales}")
print(f"You get a {bonus:.0%} bonus")
print(f"Your bonus is ${bonusamt:.2f}")
print(f"Your gross pay is ${gross:.2f}")
print(f"Your federal income tax is ${federaltaxamt:.2f}")
print(f"Your paycheck is ${paycheck:.2f}")
v = "2"
k = "8"
print(int(v) +int(k), "-", v, "=", "v"+ k)
