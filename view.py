"""View"""
__author__ = 'paul'


class View:
    """The view"""

    def __init__(self):
        """initialization """
        pass

    @staticmethod
    def display_menu():
        """ Main menu """

        print(""" Main menu
        1. Show books
        2. Show authors
        3. Add book
        4. Add author
        5. Add genre
        6. Delete by name
        7. Delete by ID
        8. Find a book
        9. Find an author
        ------------------------

        not working

        10. serialize to Pickle
        11. serialize to JSON
        12. deserialize from Pickle
        13. deserialize from JSON
        -----------------------
        10. quit
        """)

    @staticmethod
    def print_smth(smth):
        print(smth)
