class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' by {book.author} added to the library.")

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"Book '{book.title}' removed from the library.")
                return
        print(f"Book '{title}' not found in the library.")

    def display_books(self):
        if self.books:
            print("Books in the library:")
            for book in self.books:
                print(f"'{book.title}' by {book.author}")
        else:
            print("The library is empty.")

def main():
    library = Library()

    while True:
        print("\nLibrary System Menu:")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Display Books")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            book = Book(title, author)
            library.add_book(book)
        elif choice == "2":
            title = input("Enter book title to remove: ")
            library.remove_book(title)
        elif choice == "3":
            library.display_books()
        elif choice == "4":
            print("Exiting the library system.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
