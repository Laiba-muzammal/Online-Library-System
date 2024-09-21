# This program is for an online library system. The Library class has different features to manage books, borrowing, and wishlists.

# Here’s what you can do with the Library:
# 1. Display books: See all the books available in the library.
# 2. Search for a book: Check if a specific book is in the library.
# 3. Add a book: Add a new book to the library if it’s not already there.
# 4. Remove a book: Take a book out of the library.
# 5. Borrow a book: Take a book to read and add it to your borrowed list.
# 6. Show borrowed books: See all the books you have borrowed.
# 7. Return a book: Give back a book you borrowed.
# 8. Show wishlist: See books you want to borrow later.
# 9. Add to wishlist: Add a book from the library to your wishlist.
# 10. Remove from wishlist: Take a book out of your wishlist.
# 11. Exit: Leave the program.

# You can interact with the library by choosing options from the main menu. 
# Keep using the library until you decide to exit.


class Library:
    def __init__(self):
        self.number_of_books=0
        self.books=[]
        self.borrow=[]
        self.wishlist=[]
        
    def display_book(self):
        if not self.books:
            print("The library is empty")
        else:
            print(f"Following are the {self.number_of_books} books available in the library:")
            for book in self.books:
                print(f"- {book}")
    
    def search_book(self):
        search=input("Enter the book you want to search: ")
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
            print(f"{book} is in the wishlist. Remove it from the wishlist before adding.")
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
            print(f"{borrow} is in your wishlist. You may want to remove it from your wishlist before borrowing.")
        elif borrow in self.books:
            print(f"Yes, {borrow} is available in the library.")
            ans = input("Do you want to add it to your borrow list? (1. Yes / 2. No): ")
            if ans == "1":
                self.borrow.append(borrow)
                self.books.remove(borrow)
                self.number_of_books -= 1
                print(f"{borrow} has been added to your borrow list.")
            else:
                print("Okay.")
        else:
            print(f"Oops, {borrow} is not available in the library.")

    def display_borrow_list(self):      
        if self.borrow:
            print(f"Your borrow list contains: ")
            for book in self.borrow:
                print(f"- {book}")
        else:
            print("Your borrow list is empty.")
            
    def return_book(self):
        book=input("Enter the name of the book you want to return:")
        if book in self.borrow:
            self.borrow.remove(book)
            self.number_of_books+=1
            self.books.append(book)
            print("Book returned successfully")
        else:
            print(f"{book} not found in the borrow list")
        
    def display_wishlist(self):
        if self.wishlist:
            print("Your wishlist contains:")
            for book in self.wishlist:
                print(f"- {book}")
        else:
            print("Oops!... No books in your wishlist.")
            
    def add_wishlist(self):
        book=input("Enter the book you want to add in your wishlist: \n(Note: Only those books can be added into your wishlist that are available in the library)")
        if book in self.wishlist:
            print(f"{book} is already in your wishlist")
        elif book in self.books:
            self.wishlist.append(book)
            print("Wishlist Updated Successfully!")
        else:
            print("Oops!...Book is not available in the libraray")
                
    def remove_wishlist(self):
        book=input ("Enter the book you want to remove from your wishlist: ")
        if book in self.wishlist:
            self.wishlist.remove(book)
            print("Wishlist Updated Successfully!")
        else:
            print("Oops!...Book doesnot exist in your wihslist")
            
    def exit_library(self):
        ans = input("Are you sure you want to exit? (1. Yes / 2. No): ")
        if ans == "1":
            print("Goodbye!")
            exit()
        else:
            print("Returning to the main menu.")

                
new_book=Library()
again='y'
while(again=='y'):
    print("\n>>>Welcome To The Online Library<<<")
    print("*****MAIN MENU*****")
    print("1.Display Books List \n2.Search Book \n3.Add Book \n4.Remove Book \n5.Borrow book \n6.Display My Borrow List \n7.Return Book \n8.Display Wishlist \n9.Add To Wishlist \n10.Remove From Wishlist\n11.Exit")
    option=input("Choose your option: ")

    match (option):
        case "1":
            new_book.display_book()
        case "2":
            new_book.search_book()
        case "3":
            new_book.add_book()
        case "4":
            new_book.remove_book()
        case "5":
            new_book.borrow_book()
        case "6":
            new_book.display_borrow_list()
        case "7":
            new_book.return_book()
        case "8":
            new_book.display_wishlist()
        case "9":
            new_book.add_wishlist()
        case "10":
            new_book.remove_wishlist()
        case "11":
            new_book.exit_library()
        case _:
            print("Invalid Input!")
