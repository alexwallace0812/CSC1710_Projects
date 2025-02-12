import os

def readdat(filename="labtest.txt"):
    movies = []
    if os.path.exists(filename):
        with open(filename, "r") as file:
            for line in file:
                title, year, rating, director = line.strip().split(',')
                movies.append({"title": title, "year": year, "rating": rating, "director": director})
    return movies

def writdat(movies, filename="labtest.txt"):
    with open(filename, "w") as file:
        for movie in movies:
            file.write(f"{movie['title']},{movie['year']},{movie['rating']},{movie['director']}\n")

def dismov(movies):
    print(f"{'Title':<15}{'Year':<15}{'Rating':<15}{'Director':<15}")
    print(f"{'_':_^60}")
    for i, movie in enumerate(movies, start=1):
        print(f"{i}. {movie['title']:<15}{movie['year']:<15}{movie['rating']:<15}{movie['director']:<15}")
    print(f"{'_':_^60}")

def addmov(movies):
    title = input("Enter the title: ")
    year = input("Enter the year: ")
    rating = input("Enter the rating: ")
    director = input("Enter the director: ")
    movies.append({"title": title, "year": year, "rating": rating, "director": director})
    print("Movie added successfully!")

def delmov(movies):
    display_movies(movies)
    try:
        choice = int(input("Enter the number of the movie to delete: "))
        if 1 <= choice <= len(movies):
            del movies[choice - 1]
            print("Movie deleted successfully!")
        else:
            print("Invalid choice. Please enter a valid number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def searchmov(movies):
    search_term = input("Enter the search term: ").lower()
    results = [movie for movie in movies if search_term in movie['title'].lower()]
    
    if results:
        display_movies(results)
    else:
        print("No matching movies found.")

def main():
    filename = "labtest.txt"
    movies = readdat(filename)

    while True:
        print("\nMenu:")
        print("(v)iew movies")
        print("(a)dd a movie")
        print("(d)elete a movie")
        print("(s)earch for a movie")
        print("(q)uit")

        choice = input("What would you like to do? ").lower()

        if choice == 'v':
            dismov(movies)
        elif choice == 'a':
            addmov(movies)
        elif choice == 'd':
            delmov(movies)
        elif choice == 's':
            searchmov(movies)
        elif choice == 'q':
            writdat(movies, filename)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
