labtext = open("labtest.txt", "w")
while True:
    print("***Menu***")
    print("(a)dd a movie")
    print("(d)elete a movie")
    print("(v)iew the movies")
    print("(s)earch for a movie")
    print("(q)uit")
    choice = input("What would you like to do? ")
    if choice == "q":
        break
    elif choice == "a":
        movname = input("Movie name: ")
        movyear = input("Movie year: ")
        movrate = input("Movie rating: ")
        movdir = input("Movie director: ")
        labtext.write(movname + " ")
        labtext.write(movyear + " ")
        labtext.write(movrate + " ")
        labtext.write(movdir + "\n")
    elif choice == "d":

    elif choice == "v":
        for 

    elif choice == "s":

labtext.close()
