from model import DB
import pickle

__author__ = 'Michael'


def serialization(func):
    """ decorator for Pickle serialization """
    def wrapper(data):
        """wrapper"""
        mydb = DB()
        list_authors = mydb.get_authors()
        list_books = mydb.get_books()
        list_for_serialize = {'books': list_books, 'authors': list_authors}
        with open('files/data.pickle', 'wb') as f:
            pickle.dump(list_for_serialize, f)
        func(data)
        return func
    return wrapper


def deserialization(func):
    """ decorator for Pickle deserialization """
    def wrapper(data):
        """Wrapper"""
        func(data)
        with open('files/data.pickle', 'rb') as f:
            data = pickle.load(f)
            return func
    return wrapper
