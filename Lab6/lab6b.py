print("Welcome to the parking garage")
hours = int(input("How many hours will you park?"))
cost = 10
if hours <= 4:
    print("We'll charge you for 4 hours")
elif hours > 4 and hours <= 8:
    cost = cost + 5
    print("We'll charge you for 8 hours")
elif hours > 8 and hours <= 12:
    cost = cost + 10
    print("We'll charge you for 12 hours")
elif hours > 12:
    cost + cost + 15
    print("We'll charge you for 16 hours")
detail = input("Would you like you car detailed? (y or n) ")
if detail == "y":
    cost = cost + 5
elif detail == "n":
    print("Your loss")
print(f"Your parking will cost ${cost:.2f}")
