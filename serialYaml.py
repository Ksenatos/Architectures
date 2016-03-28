# import pyaml
# import yaml
from model import DB

__author__ = 'Michael'


def serialization(func):
    """ decorator for Yaml serialization """
    def wrapper(data):
        """wrapper"""
        mydb = DB()
        list_authors = mydb.get_authors()
        list_books = mydb.get_books()
        list_for_serialize = {'books': list_books, 'authors': list_authors}
        with open('files/data.yml', 'wb') as f:
            pyaml.dump(list_for_serialize, f)
        func(data)
        return func
    return wrapper


def deserialization(func):
    """ decorator for Yaml deserialization """
    def wrapper(data):
        """wrapper"""
        func(data)
        with open('files/data.yml', 'rb') as f:
            data = yaml.load(f)

        return func
    return wrapper
