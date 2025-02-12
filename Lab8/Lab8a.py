cycle = "notdone"
names = []
print("Welcome to name search")
while cycle != "done":
    newname = input("Enter a name into the list (or done to stop): ")
    if newname == "done":
        break
    elif newname != "done":
        names.append(newname)
print("You entered the following names:")
for i in range(len(names)):
    print(names[i])



for j in range(len(names)):
    searchyn = ""
    searchname = input("Search a name in the list: ")
    if searchname == names[j]:
        print(searchname, "is in the list.")
    else:
        print(searchname, "is not in the list.")
    while not(searchyn in ["y","n"]):
        searchyn = input("Do you want to search another name? (y or n) ")
    if searchyn == "n":
        break
