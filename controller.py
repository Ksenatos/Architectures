from model import DB
from view import View

__author__ = 'paul'


class Controller:
    def __init__(self):
        self.view = View()
        self.mydb = DB()
        self.choises = {1: self.show_books,
                        2: self.show_authors,
                        3: self.add_book,
                        4: self.add_author,
                        5: self.quit}

    def run(self):
        while True:
            self.view.display_menu()
            choices = input("Enter an option: ")
            action = self.choises.get(choices)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choices))

    def show_books(self):
        for i in self.mydb.get_books():
            self.view.print_smth(i)

    def show_authors(self):
        for i in self.mydb.get_authors():
            self.view.print_smth(i)

    def add_book(self):
        books_name = input('Enter books_name: ')
        authors_id = input('Authors_id: ')
        self.mydb.add_book(books_name, int(authors_id))

    def add_author(self):
        authors_name = input('Enter authors name: ')
        authors_lastname = input('Enter authors last name: ')
        authors_age = input('Enter authors age: ')
        self.mydb.add_author(authors_name, authors_lastname, int(authors_age))

    @staticmethod
    def quit():
        print("Bye")
        quit()

if __name__ == "__main__":
    Controller().run()
