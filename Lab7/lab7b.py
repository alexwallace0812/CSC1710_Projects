import random
print("*** Rock, Paper, Scissors. Let's Play!")
playagain = "y"
while playagain=="y":
    print("Rock, Paper, Scissors, Shoot!")
    move = input("Choose r, p, s: ")
    commove = randomrandint(1, 3)
    if commove == 1:
        commove = "Rock"
    elif commove == 2:
        commove = "Paper"
    elif commove == 3:
        commove = "Scissors"

