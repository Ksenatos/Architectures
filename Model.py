__author__ = 'paul'
last_id = 0
class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author
        global last_id
        last_id += 1
        self.id = last_id
class library:
    def __init__(self):
        self.books = []
    def new_book(self, name_of_the_new_book, author_of_the_new_book):
        self.books.append(Book(name_of_the_new_book,author_of_the_new_book))
    def find_book(self,id = 0, name_of_the_searching_book = none, author_of_the_searching_book = none):
        for book in self.books:
            if (str(id)==str(book.id)) or (str(name_of_the_searching_book) == str(book.name)) or (str(author_of_the_searching_book)== str(book.author))
                return book
            return None
