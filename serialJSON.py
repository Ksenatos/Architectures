__author__ = 'Michael'
import json
from model import DB

def makeJSONSerialize():
    mydb = DB()
    listAuthors = mydb.get_authors()
    listBooks = mydb.get_books()

    listForSerialize = {'books': listBooks, 'authors': listAuthors}

    with open('files/basic.json', mode='w', encoding='utf-8') as f:
        json.dump(listForSerialize, f)

def getJSONDeserialize():
    with open('files/basic.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    listBooks = data['books']
    listAuthors = data['authors']

    return listBooks, listAuthors

# example

# makeJSONSerialize()
#
# lista, listb = getJSONDeserialize()
# print(lista)
# print(listb)
