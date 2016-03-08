"""conroller module"""
from model import DB
from view import View
import coverage




__author__ = 'paul'


class Controller:
    def __init__(self):
        """ Initialization func"""

        self.view = View()
        self.mydb = DB()
        self.choises = {1: self.show_books,
                        2: self.show_authors,
                        3: self.add_book,
                        4: self.add_author,
                        5: self.quit}

    def run(self):
        """func run show menu on a display. This func call func display_menu from class view in view.py
           if user enter incorrect number func give error"""

        while True:
            self.view.display_menu()
            choices = input("Enter an option: ")
            action = self.choises.get(choices)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choices))

    def show_books(self):
        """func show_books get list of books. This func call func get_books from class my.db in model.py.
         Variable i goes across row in table books"""

        for i in self.mydb.get_books():
            self.view.print_smth(i)

    def show_authors(self):
        """func show_authors get list of authors. This func call func get_authors from class mydb in model.py.
         Variable i goes across row in table author"""

        for i in self.mydb.get_authors():
            self.view.print_smth(i)

    def add_book(self):
        """func add_book add book in table book. vars books_name and authors_id input by user.
        This func call func add_book from class mydb in model.py"""

        books_name = input('Enter books_name: ')
        authors_id = input('Authors_id: ')
        self.mydb.add_book(books_name, int(authors_id))

    def add_author(self):
        """func add_author add author in table author. vars authors_name, authors_lastname and authors_age input by user.
        This func call func add_author from class mydb in model.py"""

        authors_name = input('Enter authors name: ')
        authors_lastname = input('Enter authors last name: ')
        authors_age = input('Enter authors age: ')
        self.mydb.add_author(authors_name, authors_lastname, int(authors_age))

    @staticmethod
    def quit():
        """func quit exit from program"""

        print("Bye")
        quit()

if __name__ == "__main__":
    Controller().run()
