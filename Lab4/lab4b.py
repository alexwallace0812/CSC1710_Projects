name1 = input("What is your first item? ")
price1 = float(input("How much does it cost? "))
quan1 = int(input("How many do you have? "))
name2 = input("What is your second item? ")
price2 = float(input("How much does it cost? "))
quan2 = int(input("How many do you have? "))
name3 = input("What is your third item? ")
price3 = float(input("How much does it cost? "))
quan3 = int(input("How many do you have? "))
cost1 = price1*quan1
cost2 = price2*quan2
cost3 = price3*quan3
subtot = cost1+cost2+cost3
statetax = .0475
tax = subtot*statetax
tot = subtot+tax
print(f"{'Item':15}{'Price':10}{'Quantity':15}{'Cost':4}")
print(f"{'_':_^44}")
print(f"{name1:<15}{price1:>10.2f}{quan1:>15}{cost1:>4.2f}")
print(f"{name2:<12}{price2:>8.2f}{quan2:>13}{cost2:>11.2f}")
print(f"{name3:<12}{price3:>8.2f}{quan3:>13}{cost3:>11.2f}")
print(f"{'_':_^44}")
print(f"{'Subtotal:':>33}{subtot:>11.2f}")
print(f"{'Tax:':>33}{tax:>11.2f}")
print(f"{'Total:':>33}{tot:>11.2f}")

