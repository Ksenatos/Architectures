"""Classes"""
# coding=utf-8
__author__ = 'Michael'


class Author(object):
    """class Author """
    def __init__(self, id_author, fname, lname):
        """initialization"""
        self.id_author = id_author
        self.fname = fname
        self.lname = lname


class Book(object):
    """class book"""
    def __init__(self, id_book, name, id_author, id_genre):
        """iniialization"""
        self.id_author = id_author
        self.id_genre = id_genre
        self.id_book = id_book
        self.name = name


class Genre(object):
    """class ganre"""
    def __init__(self, id_genre, name):
        """initialization"""
        self.id_genre = id_genre
        self.name = name


# пример обращение к классу

# a = Author(1, "Mike", "gg")
# print(a.fname)
