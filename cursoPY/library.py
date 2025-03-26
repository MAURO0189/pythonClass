class Book: 
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            print(f'{self.title} borrowed')
        else:
            print(f'{self.title} is not available')

    def return_book(self):
        if not self.available:
            self.available = True
            print(f'{self.title} returned')
        else:
            print(f'{self.title} was not borrowed')


class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print(f'The book{book.title} is not available')

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print(f'The book {book.title} was not borrowed by {self.name}')


class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)
        print(f'The book{book.title} added to the library')

    def register_user(self, user):
        self.users.append(user)
        print(f'The user{user.name} registered in the library')

    def search_book(self, title):
            for book in self.books:
                if book.title == title:
                    return book
            return None  

    def search_user(self, name):
            for user in self.users:
                if user.name == name:
                    return user
            return None

    def show_available_books(self):
        for book in self.books:
            if book.available:
                print(f'The book{book.title} by {book.author} is available')
            else:
                print(f'The book{book.title} by {book.author} is not available')


# llamado a los metodos
book1 = Book('Python for beginners', 'David')
book2 = Book('Python for experts', 'David')

user1 = User('Mauro', 1)


library = Library()
library.add_book(book1)
library.add_book(book2)
library.register_user(user1)

library.show_available_books()

user1.borrow_book(book1)
library.show_available_books()

user1.return_book(book1)
library.show_available_books()
                    
        