labtext = open("labtest.txt", "w")
loop = ""
while True:
    loop = input("(a)dd a movie" + "\n" + "(q)uit" + "\n")
    if loop == "q":
        break
    if loop == "a":
        movname = input("Movie name: ")
        movyear = input("Movie year: ")
        movrate = input("Movie rating: ")
        movdir = input("Movie director: ")
        labtext.write(movname + " ")
        labtext.write(movyear + " ")
        labtext.write(movrate + " ")
        labtext.write(movdir + " ")
labtext.close()
