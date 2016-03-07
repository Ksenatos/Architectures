# coding=utf-8
import MySQLdb as mdb

__author__ = 'Michael'


class DB(object):
    def __init__(self):
        self.connection = None

    def connect(self):
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
        if self.connection is not None:
            self.connection.close()
        self.connection = None

    def get_authors(self):
        self.connect()
        if self.connection is None:
            return []
        cur = self.connection.cursor(mdb.cursors.DictCursor)
        cur.execute("SELECT * FROM author;")
        self.close()
        return cur.fetchall()

    def get_books(self):
        self.connect()
        if self.connection is None:
            return []
        cur = self.connection.cursor(mdb.cursors.DictCursor)
        cur.execute("SELECT b.name, b.publisher_date,"
                    "a.fname, a.lname, a.age FROM book b"
                    "INNER JOIN author a ON b.id_author = a.id_author;")
        self.close()
        return cur.fetchall()

    def add_author(self, fname, lname, age):
        self.connect()
        cur = self.connection.cursor(mdb.cursors.DictCursor)
        cur.execute("INSERT INTO author VALUES "
                    "(NULL, '%s', '%s', '%s');" % (fname, lname, age))
        cur.execute("commit")
        self.close()

    def add_book(self, name, id_author):
        self.connect()
        cur = self.connection.cursor(mdb.cursors.DictCursor)
        cur.execute("INSERT INTO book VALUES "
                    "(NULL, '%s', DATE(NOW()), '%s');" % (name, id_author))
        cur.execute("commit")
        self.close()


# остальные запросы сделаю позже
# вот пример кода как можно кидать запросы
#
# mydb = DB()

# mydb.add_author("Tony", "Stark", 45)

# выбираем автора по id его, оно авто инкрементное
# mydb.add_book("Nano", 1)

# for i in mydb.get_books():
# print(i)
