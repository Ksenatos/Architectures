import json
from model import DB

__author__ = 'Michael'


def serialization(func):
    """ decorator for JSON serialization """
    def wrapper(data):
        """wrapper"""
        print('json s-on')
        mydb = DB()
        list_authors = mydb.get_authors()
        list_books = mydb.get_books()
        list_for_serialize = {'books': list_books, 'authors': list_authors}
        with open('files/basic.json', mode='w', encoding='utf-8') as f:
            json.dump(list_for_serialize, f)
        func(data)
        return func
    return wrapper


def deserialization(func):
    """ decorator for JSON deserialization """
    def wrapper(data):
        """wrapper"""
        print('json des-on')
        func(data)
        with open('files/basic.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        # print(data)

        return func
    return wrapper
