class Library:
    def __init__(self):
        self.number_of_books = 0
        self.books = []
        self.borrow = []
        self.wishlist = []

    def display_book(self):
        if not self.books:
            print("The library is empty")
        else:
            print(f"Following are the {self.number_of_books} books available in the library:")
            for book in self.books:
                print(f"- {book}")

    def search_book(self):
        search = input("Enter the book you want to search: ")
        if search in self.books:
            print(f"Yes, {search} is available in the library")
        else:
            print(f"Oops, {search} is not available in the library")

    def add_book(self):
        book = input("Enter the book you want to add: ")
        if book in self.books:
            print(f"{book} already exists in the library.")
        elif book in self.borrow:
            print(f"{book} is currently borrowed. Return it before adding.")
        elif book in self.wishlist:
            print(f"{book} is in the wishlist. Remove it before adding.")
        else:
            self.books.append(book)
            self.number_of_books += 1
            print(f"{book} has been added to the library.")

    def remove_book(self):
        dlt = input("Enter the book you want to delete: ")
        if dlt in self.books:
            self.books.remove(dlt)
            self.number_of_books -= 1
            print(f"{dlt} has been removed from the library.")
        else:
            print(f"{dlt} not found in the library.")

    def borrow_book(self):
        borrow = input("Enter the book you want to borrow: ")
        if borrow in self.borrow:
            print(f"{borrow} is already in your borrow list.")
        elif borrow in self.wishlist:
            print(f"{borrow} is in your wishlist. Remove it before borrowing.")
        elif borrow in self.books:
            print(f"Yes, {borrow} is available.")
            ans = input("Do you want to borrow it? (1. Yes / 2. No): ")
            if ans == "1":
                self.borrow.append(borrow)
                self.books.remove(borrow)
                self.number_of_books -= 1
                print(f"{borrow} has been added to your borrow list.")
            else:
                print("Okay.")
        else:
            print(f"{borrow} is not available in the library.")

    def display_borrow_list(self):
        if self.borrow:
            print("Your borrow list contains:")
            for book in self.borrow:
                print(f"- {book}")
        else:
            print("Your borrow list is empty.")

    def return_book(self):
        book = input("Enter the name of the book to return: ")
        if book in self.borrow:
            self.borrow.remove(book)
            self.books.append(book)
            self.number_of_books += 1
            print("Book returned successfully.")
        else:
            print(f"{book} not found in the borrow list")

    def display_wishlist(self):
        if self.wishlist:
            print("Your wishlist contains:")
            for book in self.wishlist:
                print(f"- {book}")
        else:
            print("No books in your wishlist.")

    def add_wishlist(self):
        book = input("Enter book to add to wishlist:\n(Note: Only available books can be added): ")
        if book in self.wishlist:
            print(f"{book} is already in your wishlist")
        elif book in self.books:
            self.wishlist.append(book)
            print("Wishlist updated successfully!")
        else:
            print("Book not available in the library.")

    def remove_wishlist(self):
        book = input("Enter book to remove from wishlist: ")
        if book in self.wishlist:
            self.wishlist.remove(book)
            print("Wishlist updated successfully!")
        else:
            print("Book not found in your wishlist")

    def exit_library(self):
        ans = input("Are you sure you want to exit? (1. Yes / 2. No): ")
        if ans == "1":
            print("Goodbye!")
            exit()
        else:
            print("Returning to menu.")
