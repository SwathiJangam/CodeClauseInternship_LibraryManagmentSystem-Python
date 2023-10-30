class Library:
    def __init__(self, list_of_books):
        self.available_books = list_of_books

    def display_available_books(self):
        print("Available Books:")
        for book in self.available_books:
            print(book)

    def lend_book(self, requested_book):
        if requested_book in self.available_books:
            print("You have borrowed the book.")
            self.available_books.remove(requested_book)
        else:
            print("Sorry, the book is not available in our library.")

    def add_book(self, returned_book):
        self.available_books.append(returned_book)
        print("You have returned the book. Thank you!")

class Customer:
    def request_book(self):
        print("Enter the name of a book you would like to borrow: ")
        self.book = input()
        return self.book

    def return_book(self):
        print("Enter the name of the book you are returning: ")
        self.book = input()
        return self.book

library = Library(["Python Programming", "Java Programming", "Web Development", "Machine Learning"])
customer = Customer()

while True:
    print("Enter 1 to display the available books")
    print("Enter 2 to request for a book")
    print("Enter 3 to return a book")
    print("Enter 4 to exit")
    user_choice = int(input())
    if user_choice == 1:
        library.display_available_books()
    elif user_choice == 2:
        requested_book = customer.request_book()
        library.lend_book(requested_book)
    elif user_choice == 3:
        returned_book = customer.return_book()
        library.add_book(returned_book)
    elif user_choice == 4:
        break
