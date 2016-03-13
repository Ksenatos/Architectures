# coding=utf-8
__author__ = 'Michael'


class Author(object):
    def __init__(self, id_author, fname, lname):
        self.id_author = id_author
        self.fname = fname
        self.lname = lname


class Book(object):
    def __init__(self, id_book, name, id_author, id_genre):
        self.id_author = id_author
        self.id_genre = id_genre
        self.id_book = id_book
        self.name = name


class Genre(object):
    def __init__(self, id_genre, name):
        self.id_genre = id_genre
        self.name = name


# пример обращение к классу

# a = Author(1, "Mike", "gg")
# print(a.fname)
