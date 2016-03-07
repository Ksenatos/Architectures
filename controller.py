__author__ = 'paul'
from model import DB
from view import View
class Controller:
    def __init__(self):
        self.view = View()
        self.mydb = DB()
        self.choises = {1: self.Show_books, 2: self.Show_authors, 3: self.Add_book, 4: self.Add_author, 5: self.Quit}
    def run(self):
        while True:
            self.view.display_menu()
            choices = input("Enter an option: ")
            action = self.choises.get(choices)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choices))
    def Show_books(self):
        for i in self.mydb.get_books():
            print(i)

    def Show_authors(self):
        for i in self.mydb.get_authors():
            print(i)

    def Add_book(self):
        books_name = input('Enter books_name: ')
        authors_id = input('Authors_id: ')
        self.mydb.add_book(books_name, int(authors_id))

    def Add_author(self):
        authors_name = input('Enter authors name: ')
        authors_lastname = input('Enter authors last name: ')
        authors_age = input('Enter authors age: ')
        self.mydb.add_author(authors_name, authors_lastname, int(authors_age))

    def Quit(self):
        print("Bye")
        quit()

if __name__ == "__main__":
    Controller().run()