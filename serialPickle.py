__author__ = 'Michael'
from model import DB
import pickle


def makePickleSerialization():
    mydb = DB()
    listAuthors = mydb.get_authors()
    listBooks = mydb.get_books()

    listForSerialize = {'books': listBooks, 'authors': listAuthors}
    with open('files/data.pickle', 'wb') as f:
        pickle.dump(listForSerialize, f)


def getPickleDeserialize():
    with open('files/data.pickle', 'rb') as f:
        data = pickle.load(f)

    listBooks = data['books']
    listAuthors = data['authors']

    return listBooks, listAuthors


#   example

# makePickleSerialization()
#
# lista, listb = getPickleDeserialize()
#
# print(lista)
# print(listb)

