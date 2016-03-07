__author__ = 'paul'


class View:
    def __init__(self):
        pass

    @staticmethod
    def display_menu():
        print(""" Main menu
        1. Show books
        2. Show authors
        3. Add book
        4. Add author
        5. Quit
        """)

    @staticmethod
    def print_smth(smth):
        print(smth)
