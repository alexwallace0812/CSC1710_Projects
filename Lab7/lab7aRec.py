print("*** Welcome to the donut swhop ***")
print("\n")
numdon = 0
while numdon<=0:
    numdon = int(input("How many donuts would you like? "))
    if numdon<0:
        print("Please enter a positive number")
if numdon==1:
    print("You will get 1 donut")
else:
    print(f"You will get {numdon} donuts")
sprin = input("Would you like spinkles (y or n)? ")
while not(sprin=="y") and not(sprin=="n"):
    sprin = input("Would you like sprinkles (y or n)? ")
if sprin=="y":
    print(f"Okay. {numdon} donuts with sprinkles.")
elif sprin=="n":
    print(f"Okay. {numdon} donuts without sprinkles.")
donutcost = 1.25
totcost = numdon*donutcost
if sprin=="y":
    totcost=totcost+(numdon*.1)
print(f"That will cost ${totcost:.2f}")
