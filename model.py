# coding=utf-8
import coverage
import MySQLdb as mdb

__author__ = 'Michael'


class DB(object):
    def __init__(self):
        """initialization

        >>> __init__(mdb)
        mdb.connection == None

        >>> __init__(None)
        Traceback (most recent call last):
        Initialization error: initialization is failed
        """
        self.connection = None

    def connect(self):
        """func connect provide connection between, database
         witch was created in MySQL server, and object mdb

        >>> mdb.connection() is None
        Traceback (most recent call last):
        connection error: connection is failed

        """
        if self.connection is not None:
            return
        try:
            self.connection = mdb.connect('127.0.0.1',
                                          'root',
                                          '1111',
                                          'library')

        except mdb.Error, e:
            print "Error %d: %s change password" % (e.args[0], e.args[1])
            self.connection = None

    def close(self):
        """Disconnect database and object mdb

        >>> mdb.connection is None
        Traceback (most recent call last):
        Connection error: already disconnect

        """
        if self.connection is not None:
            self.connection.close()
        self.connection = None

    def get_authors(self):
        """func get_authors get list of authors from table author,
         if connection was successfull

         >>> mdb.connection() is None
         Traceback (most recent call last):
         connection error: connection is failed


         """

        self.connect()
        if self.connection is None:
            return []
        cur = self.connection.cursor(mdb.cursors.DictCursor)
        cur.execute("SELECT * FROM author;")
        self.close()
        return cur.fetchall()

    def get_books(self):
        """func get_books get list of books from table books,
        if connection was successfull

        >>> mdb.connection() is None
        Traceback (most recent call last):
        connection error: connection is failed
        """
        self.connect()
        if self.connection is None:
            return []
        cur = self.connection.cursor(mdb.cursors.DictCursor)
        cur.execute("SELECT b.name, b.publisher_date,"
                    "a.fname, a.lname, g.name from book b "
                    "inner join author a inner join genre g "
                    "where b.id_author = a.id_author "
                    "and b.id_genre = g.id_genre;")
        self.close()
        return cur.fetchall()

    def add_author(self, fname, lname):
        """func add_author add new author in table authors

        >>> add_author(mdb, 'Karl', 'JJ')
        ['Karl', 'JJ']

        """
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
                    "(NULL, '%s', DATE(NOW()), '%s', '%s');"
                    % (name, id_author, id_genre))
        cur.execute("commit")
        self.close()

    def add_genre(self, name):
        """func add_genre add new genre in table genre"""
        self.connect()
        cur = self.connection.cursor(mdb.cursors.DictCursor)
        cur.execute("INSERT INTO genre VALUES "
                    "(NULL, '%s');" % name)
        cur.execute("commit")
        self.close()

    def delete_book_by_name(self, name):
        """func delete_book_by_name delete book, from table books, which name was entered

        >>> delete_book_by_name(mdb,'Straj')
        Traceback (most recent call last):
        Error: unpredictable result
        """
        self.connect()
        cur = self.connection.cursor(mdb.cursors.DictCursor)
        cur.execute("DELETE FROM book WHERE "
                    "name = '%s');" % name)
        cur.execute("commit")
        self.close()

    def delete_book_by_id(self, id_book):
        """func delete_book_by_id delete book, from table books, which Id was entered

        >>> delete_book_by_id(mdb, '1')
        Traceback (most recent call last):
        Error: unpredictable result
        """
        self.connect()
        cur = self.connection.cursor(mdb.cursors.DictCursor)
        cur.execute("DELETE FROM book WHERE "
                    "id_book = '%s');" % id_book)
        cur.execute("commit")
        self.close()

    def find_books(self, name):
        """func find_books are looking the book in table books, which name was entered

        >>> mdb.connection() is None
        Traceback (most recent call last):
        connection error: connection is failed

        >>> find_books(mdb,'Straj')
        Traceback (most recent call last):
        Error: unpredictable result

        """
        self.connect()
        symbol = '%'
        if self.connection is None:
            return []
        cur = self.connection.cursor(mdb.cursors.DictCursor)
        cur.execute("SELECT * FROM book WHERE name LIKE '%s%s%s';"
                    % (symbol, name, symbol))
        self.close()
        return cur.fetchall()

    def find_author(self, name):
        """func find_author are looking the author in table authors, whose name was entered

        >>> mdb.connection() is None
        Traceback (most recent call last):
        connection error: connection is failed

        >>> find_author(mdb, 'Pehov')
        Traceback (most recent call last):
        Error: unpredictable result
        """
        self.connect()
        symbol = '%'
        if self.connection is None:
            return []
        cur = self.connection.cursor(mdb.cursors.DictCursor)
        cur.execute("SELECT * FROM author"
                    " WHERE concat(fname, lname) LIKE '%s%s%s';"
                    % (symbol, name, symbol))
        self.close()
        return cur.fetchall()


import doctest
doctest.testmod()
