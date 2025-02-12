########################################################################
# File Name: lab9c.py
# Programmer: Alex Wallace
# Course: CSC1710 – Section 1
# Date Submitted: November 2, 2023
# Location: /home/students/awallace/csc1710/Lab9/lab9c.py
# Description: This progrom prompts the user to input item names and
# their prices at random. It then sorts either by price or name and
# outputs a parallel list
# Assistance: Paul helped me with some advanced coding tips
# Compile and Execute: Python3 lab9c.py
# Additional files: None
#######################################################################
# Setting up the program
prods = []
pric = []
pro = ""
# Asking the user to input the names and prices of items and it add it to the list
while pro != "done":
    pro = input("Enter a product name: ")
    if pro != "done":
        pri = float(input("Enter the price: "))
        prods.append(pro)
        pric.append(pri)

# This will print out the list as inputed
print(f"{'Products':<15}{'Prices':>15}")
print(f"{'_':_^30}")
for i in range(len(prods)):
    print(f"{prods[i]:<15}{pric[i]:>15}")
print("\n")
# This organizes the things into a parallel list
for i in range(len(prods)-1):
    small = prods[i]
    index = i
    for j in range(i+1, len(prods)):
        if(prods[j] < small):
            small = prods[j]
            index = j

    prods[i], prods[index] = prods[index], prods[i]
    pric[i], pric[index] = pric[index], pric[i]
# This prints out the final product and the completed parallel list
print(f"{'Products':<15}{'Prices':>15}")
print(f"{'_':_^30}")
for i in range(len(prods)):
    print(f"{prods[i]:<15}{pric[i]:>15}")
print("\n")
# This will organize the thing by price
for i in range(len(pric)-1):
    small = pric[i]
    index = i
    for j in range(i+1, len(pric)):
        if(pric[j] < small):
            small = pric[j]
            index = j

    pric[i], pric[index] = pric[index], pric[i]
    prods[i], prods[index] = prods[index], prods[i]

# This will print out the sorted by price list
print(f"{'Products':<15}{'Prices':>15}")
print(f"{'_':_^30}")
for i in range(len(prods)):
    print(f"{prods[i]:<15}{pric[i]:>15}")
print("\n")
