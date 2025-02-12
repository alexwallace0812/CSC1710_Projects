import os

def readdat(filename="labtest.txt"):
    list1 = []
    if os.path.exists(filename):
        with open(filename, "r") as file:
            for line in file:
                title, year, rating, director = line.strip().split(',')
                list1.append({"title": title, "year":  year, "rating": rating, "director": director})
    return 
    print(list1)

def display():
    print("Title\t\tYear\t\tRating\t\tDirector ")
    print(f"{'_':_^48}")
    
def main():
    read()
    display()

read()
