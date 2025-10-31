library = [
    {"title": "Munamadan", "author": "Laxmi Prasad Devkota", "available": True},
    {"title": "Palpasa Cafe", "author": "Narayan Wagle", "available": False},
    {"title": "Atomic Habits", "author": "James Clear","available": True }
]

def menu():
    print("===================== LIBRARY =====================")
    print("\n")
    print("-" * 45)
    print("SERVICES")
    print("-" * 45)
    print("1. Display all books")
    print("2. Add a new book")
    print("3. Remove a book")
    print("4. Borrow book")
    print("5. Return book")
    print("6. Leave")
    print("-" * 45)

def display_books():
    if len(library) == 0:
        print("No books in Library yet. Try again some other time")
        return
    print(f"Library have over {len(library)} book(s): ")
    for i, book in enumerate(library, start=1):
        status = "Available" if book["available"] else "Not Available"
        print(f"{i}. {book['title']} by {book['author']} - {status}")
    

def add_book():
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    library.append({"title": title, "author": author, "available" : True})
    print(f'Book "{title}" by {author} added to the library.')
    

def remove_book():
    display_books()
    try:
        book_index = int(input("Enter the number of the book to remove: "))
        if 1 <= book_index <= len(library):
            removed_book = library.pop(book_index - 1)
            print(f'Book "{removed_book["title"]}" removed from the library.')
        else:
            print("Invalid book number.")
    except ValueError:
        print("Please enter a valid number.")
    

def borrow_book():
    display_books()
    try:
        book_index = int(input("Enter the number of the book to borrow: "))
        if 1 <= book_index <= len(library):
            if library[book_index - 1]["available"]:
                library[book_index - 1]["available"] = False
                print(f'You have borrowed "{library[book_index - 1]["title"]}".')
            else:
                print("Sorry, this book is currently not available.")
        else:
            print("Invalid book number.")
    except ValueError:
        print("Please enter a valid number.")
    

def return_book():
    display_books()
    try:
        book_index = int(input("Enter the number of the book to return: "))
        if 1 <= book_index <= len(library):
            if not library[book_index - 1]["available"]:
                library[book_index - 1]["available"] = True
                print(f'You have returned "{library[book_index - 1]["title"]}".')
            else:
                print("This book was not borrowed.")
        else:
            print("Invalid book number.")
    except ValueError:
        print("Please enter a valid number.")
    

def main():
    while True:
        menu()
        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            display_books()
            input("\nPress Enter to continue...")
        elif choice == '2':
            add_book()
            input("\nPress Enter to continue...")
        elif choice == '3':
            remove_book()
            input("\nPress Enter to continue...")
        elif choice == '4':
            borrow_book()
            input("\nPress Enter to continue...")
        elif choice == '5':
            return_book()
            input("\nPress Enter to continue...")
        elif choice == '6':
            print("Thank you for using the library system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
    


