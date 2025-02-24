import json

class MovieDatabase:
    def __init__(self, filename="movies.json"):
        self.filename = filename
        self.load_movies()

    def load_movies(self):
        try:
            with open(self.filename, "r") as file:
                self.movies = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.movies = {}

    def save_movies(self):
        with open(self.filename, "w") as file:
            json.dump(self.movies, file, indent=4)

    def add_movie(self):
        title = input("Enter movie title: ")
        if title in self.movies:
            print("Movie already exists.")
            return
        genre = input("Enter genre: ")
        director = input("Enter director: ")
        release_date = input("Enter release date: ")
        actors = input("Enter actors (comma-separated): ").split(", ")
        
        self.movies[title] = {
            "genre": genre,
            "director": director,
            "release_date": release_date,
            "actors": actors
        }
        self.save_movies()
        print("Movie added successfully!")

    def edit_movie(self):
        title = input("Enter the movie title to edit: ")
        if title not in self.movies:
            print("Movie not found.")
            return
        print("Enter new details (leave blank to keep existing values):")
        
        genre = input(f"New genre ({self.movies[title]['genre']}): ") or self.movies[title]['genre']
        director = input(f"New director ({self.movies[title]['director']}): ") or self.movies[title]['director']
        release_date = input(f"New release date ({self.movies[title]['release_date']}): ") or self.movies[title]['release_date']
        actors = input(f"New actors ({', '.join(self.movies[title]['actors'])}): ")
        if actors:
            actors = actors.split(", ")
        else:
            actors = self.movies[title]['actors']
        
        self.movies[title] = {
            "genre": genre,
            "director": director,
            "release_date": release_date,
            "actors": actors
        }
        self.save_movies()
        print("Movie updated successfully!")

    def delete_movie(self):
        title = input("Enter the movie title to delete: ")
        if title in self.movies:
            del self.movies[title]
            self.save_movies()
            print("Movie deleted successfully!")
        else:
            print("Movie not found.")

    def view_movies(self):
        if not self.movies:
            print("No movies found.")
            return
        for title, details in self.movies.items():
            print(f"\nTitle: {title}")
            for key, value in details.items():
                print(f"{key.capitalize()}: {value}")

    def search_movies(self):
        criteria = input("Search by (title/director/genre/release_date/actor): ")
        value = input("Enter search value: ")
        found = False
        for title, details in self.movies.items():
            if criteria == "actor" and value in details["actors"]:
                found = True
            elif criteria in details and details[criteria] == value:
                found = True
            if found:
                print(f"\nTitle: {title}")
                for key, val in details.items():
                    print(f"{key.capitalize()}: {val}")
                found = False

    def run(self):
        while True:
            print("\nMovie Database Management System")
            print("1. Add Movie")
            print("2. Edit Movie")
            print("3. Delete Movie")
            print("4. View All Movies")
            print("5. Search Movie")
            print("6. Exit")
            choice = input("Enter choice: ")
            
            if choice == "1":
                self.add_movie()
            elif choice == "2":
                self.edit_movie()
            elif choice == "3":
                self.delete_movie()
            elif choice == "4":
                self.view_movies()
            elif choice == "5":
                self.search_movies()
            elif choice == "6":
                print("Exiting...")
                break
            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    MovieDatabase().run()
