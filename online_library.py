from library import Library

new_book = Library()
again = 'y'

while again == 'y':
    print("\n>>> Welcome To The Online Library <<<")
    print("***** MAIN MENU *****")
    print("1. Display Books List\n2. Search Book\n3. Add Book\n4. Remove Book\n5. Borrow Book\n6. Display Borrow List\n7. Return Book\n8. Display Wishlist\n9. Add To Wishlist\n10. Remove From Wishlist\n11. Exit")
    option = input("Choose your option: ")

    match option:
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
