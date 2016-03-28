import pyaml
import yaml
from model import DB

__author__ = 'Michael'

def serialization(func):

    def wrapper(data):
        mydb = DB()
        listAuthors = mydb.get_authors()
        listBooks = mydb.get_books()
        listForSerialize = {'books': listBooks, 'authors': listAuthors}
        with open('files/data.yml', 'wb') as f:
             pyaml.dump(listForSerialize, f)
        func(data)
        return func
    return wrapper

def deserialization(func):

    def wrapper(data):
        with open('files/data.yml', 'rb') as f:
            data = yaml.load(f)
        func(data)
        return func
    return wrapper







# def makeYamlSerialization():
#     mydb = DB()
#     listAuthors = mydb.get_authors()
#     listBooks = mydb.get_books()
#
#     listForSerialize = {'books': listBooks, 'authors': listAuthors}
#     with open('files/data.yml', 'wb') as f:
#         pyaml.dump(listForSerialize, f)
#
#
# def getYamlDeserialize():
#     with open('files/data.yml', 'rb') as f:
#         data = yaml.load(f)
#
#     listBooks = data['books']
#     listAuthors = data['authors']
#
#     return listBooks, listAuthors

# makeYamlSerialization()
#
# data1, data2 = getYamlDeserialize()
# print(data1)
# print(data2)
