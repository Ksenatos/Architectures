"""controller module"""
#from model import DB
from view import View
import configparser
# import coverage

__author__ = 'paul'

'''Using config to choose DB type'''
try:
    config = configparser.ConfigParser()
    config.read('files/config_for_SQL.py')
except configparser.ParsingError:
    print('could not parse')

try:
    option = config.get('ModelFile', 'ModelType')
except:
    print("exception on %s!" % option)

SQL = Lite = Postgre = False
if option == 'MySQL':
    from model import DB
    SQL = True
elif option == 'SQLite':
    from SQLite import DB
    Lite = True
elif option == 'PostgreSQL':
    from modelPost import DB
    SQL = True
else:
    print('<files/config_for_SQL.py>% wrong option')



'''Using config to choose the serialization type'''
# try:
#     config = configparser.ConfigParser()
#     config.read('files/config.py')
# except configparser.ParsingError:
#     print('could not parse')
# try:
#     option = config.get('ModelFile', 'ModelType')
# except:
#     print("exception on %s!" % option)
#
# if option == 'pickle':
#     from serialPickle import serialization
#     from serialPickle import deserialization
# elif option == 'json':
#     from serialJSON import serialization
#     from serialJSON import deserialization
# elif option == 'yaml':
#     from serialYaml import serialization
#     from serialYaml import deserialization
# else:
#     print('<files/config.py>% wrong option')


class Controller:
    """The controller """

    def __init__(self):
        """ Initialization func"""

        self.view = View()
        self.mydb = DB()
        self.choices = {#"1": self.show_books,
                        "2": self.show_authors,
                        # "3": self.add_book,
                        "4": self.add_author,
                        # "5": self.add_genre,
                        # "6": self.delete_book_by_name,
                        # "7": self.delete_book_by_id,
                        # "8": self.find_books,
                        # "9": self.find_author,
                        "10": self.quit
                        }

    def run(self):
        """func run show menu on a display.
            This func call func display_menu from class view in view.py
           if user enter incorrect number func give error"""

        while True:
            self.view.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

   # # @serialization
   #  def show_books(self):
   #      """func show_books get list of books.
   #      This func call func get_books from class my.db in model.py.
   #       Variable i goes across row in table books"""
   #
   #      for i in self.mydb.get_books():
   #          self.view.print_smth("Book name: %s" % i["name"])
   #          self.view.print_smth("Author: %s %s" % (i["fname"], i["lname"]))
   #          self.view.print_smth("Genre: %s" % i["g.name"])
   #          self.view.print_smth("--------------------------------")

  #  @serialization
    if SQL:
        def show_authors(self):
            """func show_authors get list of authors.
        This func call func get_authors from class mydb in model.py.
         Variable i goes across row in table author"""
            print(True)
            for i in self.mydb.get_authors():
                self.view.print_smth("Author: %s %s" % (i["FNAME"], i["LNAME"]))
    else:
        def show_authors(self):
            """func show_authors get list of authors.
        This func call func get_authors from class mydb in model.py.
         Variable i goes across row in table author"""
            print(True)
            for i in self.mydb.get_authors():
                self.view.print_smth("Author: %s %s %s" % (i[1], i[2], i[3]))

    #@serialization
    # def add_book(self):
    #     """func add_book add book in table book.
    #     vars books_name and authors_id input by user.
    #     This func call func add_book from class mydb in model.py"""
    #
    #     books_name = input('Enter books name: ')
    #     authors_id = input('Authors id: ')
    #     genre_id = input('Genre id: ')
    #     self.mydb.add_book(books_name, int(authors_id), int(genre_id))
    #
    # #@serialization
    def add_author(self):
        """func add_author add author in table author.
         vars authors_name, authors lastname and authors_age input by user.
        This func call func add_author from class mydb in model.py"""

        authors_name = input('Enter authors name: ')
        authors_lastname = input('Enter authors last name: ')
        # authors_age = input('Enter authors age: ')
        self.mydb.add_author(authors_name, authors_lastname)
    #
    # #@serialization
    # def add_genre(self):
    #     """func add genre in table genre. vars genre name input by user.
    #     This func call func add_book from class mydb in model.py"""
    #
    #     genres_name = input('Enter a new genre: ')
    #     self.mydb.add_genre(genres_name)
    #
    # #@serialization
    # def delete_book_by_name(self):
    #     """func delete book in table books by name."""
    #     books_name = input('Enter books name: ')
    #     self.mydb.delete_book_by_name(books_name)
    #
    # #@serialization
    # def delete_book_by_id(self):
    #     """func delete book in table books my Id"""
    #     books_id = input('Enter books ID: ')
    #     self.mydb.delete_book_by_id(int(books_id))
    #
    # #@deserialization
    # def find_books(self):
    #     """func searching book by part of its name"""
    #     books_name = input('Search: ')
    #     self.view.print_smth(self.mydb.find_books(books_name))
    #
    # #@deserialization
    # def find_author(self):
    #     """ffunc searching book by part of his name"""
    #     authors_name = input('Search: ')
    #     self.view.print_smth(self.mydb.find_author(authors_name))
    #
    #@staticmethod
    def quit(self):
        """func quit exit from program"""

        print("Bye")
        quit()


if __name__ == "__main__":
    Controller().run()
