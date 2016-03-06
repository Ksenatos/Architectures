__author__ = 'paul'
from Model import Library, Book
from View import View

class Controller:
    def __init__(self):
        self.view = View()
        self.librery = Library()
        self.choises = {1: self.show_the_books, 2: self.add_book,  3: self.find_book, 4: self.quit}
    def run (self):
        while True:
            self.view.main_menu()
            choises = input("Enter an option ")
            action = self.choises.get(choises)
            if action:
                action()
            else:
                print("{0} is not a valied choice".format(choises))

    def show_the_books (self, books = None):
        if not books:
            books = self.librery.books
            for book in books:
                print("{0}: {1}\n{2}".format(
                    book.id, book.name, book.author))

    def add_book (self):
        record = input("enter a record ")
        self.librery.new_book(record)
        print("Your record has been added")
    def find_book(self):
        pass
    def quit(self):
        print("Bye")

if __name__ == "__main__":
     Controller().run()



