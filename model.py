# coding=utf-8
import MySQLdb as mdb

__author__ = 'Michael'


class DB(object):
    def __init__(self):
        self.connection = None

    def connect(self):
        """func connect provide connection between, database witch was created in MySQL server, and object mdb """
        if self.connection is not None:
            return
        try:
            self.connection = mdb.connect('127.0.0.1',
                                          'root',
                                          'May the force be with you',
                                          'library')

        except mdb.Error, e:
            print "Error %d: %s fuck" % (e.args[0], e.args[1])
            self.connection = None

    def close(self):
        """Disconnect database and object mdb"""
        if self.connection is not None:
            self.connection.close()
        self.connection = None

    def get_authors(self):
        """func get_authors get list of authors from table author, if connection was successfull"""

        self.connect()
        if self.connection is None:
            return []
        cur = self.connection.cursor(mdb.cursors.DictCursor)
        cur.execute("SELECT * FROM author;")
        self.close()
        return cur.fetchall()

    def get_books(self):
        """func get_books get list of books from table books, if connection was successfull"""
        self.connect()
        if self.connection is None:
            return []
        cur = self.connection.cursor(mdb.cursors.DictCursor)
        cur.execute("SELECT b.name, b.publisher_date,"
                    "a.fname, a.lname FROM book b "
                    "INNER JOIN author a ON b.id_author = a.id_author;")
        self.close()
        return cur.fetchall()

    def add_author(self, fname, lname):
        """func add_author add new author in table authors """
        self.connect()
        cur = self.connection.cursor(mdb.cursors.DictCursor)
        cur.execute("INSERT INTO author VALUES "
                    "(NULL, '%s', '%s');" % (fname, lname))
        cur.execute("commit")
        self.close()

    def add_book(self, name, id_author, id_genre):
        """func add_book add new book in table books"""
        self.connect()
        cur = self.connection.cursor(mdb.cursors.DictCursor)
        cur.execute("INSERT INTO book VALUES "
                    "(NULL, '%s', DATE(NOW()), '%s', '%s');" % (name, id_author, id_genre))
        cur.execute("commit")
        self.close()

    def add_genre(self, name):
        self.connect()
        cur = self.connection.cursor(mdb.cursors.DictCursor)
        cur.execute("INSERT INTO genre VALUES "
                    "(NULL, '%s');" % name)
        cur.execute("commit")
        self.close()

    def delete_book_by_name(self, name):
        self.connect()
        cur = self.connection.cursor(mdb.cursors.DictCursor)
        cur.execute("DELETE FROM book WHERE "
                    "name = '%s');" % name)
        cur.execute("commit")
        self.close()

    def delete_book_by_id(self, id_book):
        self.connect()
        cur = self.connection.cursor(mdb.cursors.DictCursor)
        cur.execute("DELETE FROM book WHERE "
                    "id_book = '%s');" % id_book)
        cur.execute("commit")
        self.close()

    def find_books(self, name):
        self.connect()
        symbol = '%'
        if self.connection is None:
            return []
        cur = self.connection.cursor(mdb.cursors.DictCursor)
        cur.execute("SELECT * FROM book WHERE name LIKE '%s%s%s';" % (symbol, name, symbol))
        self.close()
        return cur.fetchall()

    def find_author(self, name):
        self.connect()
        symbol = '%'
        if self.connection is None:
            return []
        cur = self.connection.cursor(mdb.cursors.DictCursor)
        cur.execute("SELECT * FROM author WHERE concat(fname, lname) LIKE '%s%s%s';" % (symbol, name, symbol))
        self.close()
        return cur.fetchall()


# остальные запросы сделаю позже
# вот пример кода как можно кидать запросы
#
# mydb = DB()

# выбираем автора по id его, оно авто инкрементное

# можем искать даже по части имени
# вот пример

<<<<<<< HEAD
# print(mydb.get_books())
=======
>>>>>>> origin/master
# print(mydb.find_books("Na"))
# print(mydb.find_author("To"))


# проверьте только удаление работает ли у вас, я не проверял
