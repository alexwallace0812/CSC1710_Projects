print("Welcome to the post office!")
print("\n")
state = input("Will your package be staying in state (yes or no)")
weight = float(input("Enter a weight in pounds: "))
priority = input("Choose a priority (1, 2, 3): ")
if priority == "1":
    price = weight*5
elif priority == "2":
    price = weight*3
elif priority == "3":
    price = weight*1
if state == "no":
    price = price*2
print("Thank you!")
print(f"Your package will cost ${price:.2f} to ship")
