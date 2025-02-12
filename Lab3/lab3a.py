stock = int(input("how many cars do you have in stock?"))
trailer = int(input("How many cars fit on a trailer"))
fulltrailers = stock//trailer
leftcats = stock%trailer
print("You will have", str(fulltrailers), "and", str(leftcats), "leftover cars")

