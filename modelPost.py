"""Model"""
# coding=utf-8
# import coverage

import psycopg2
import sys



class DB(object):

  def __init__(self):
   self.con = None

  def connect (self):
   try:
     psycopg2.connect(database="test", user="postgres", password="1111", host="127.0.0.1", port="5432")
   except:
     print "I am unable to connect to the database"
     self.con = None


  def close(self):
        """Disconnect database and object mdb
        """
        if self.con is not None:
            self.con.close()
        self.con = None

  def get_authors(self):
        """func get_authors get list of authors from table author,
         if connection was successfull   """

        self.connect()
        if self.con is None:
            return []
        cur = self.con.cursor()
        cur.execute("SELECT * FROM author;")
        self.close()
        return cur.fetchall()


  def add_author(self, fname, age, genre):
        """func add_author add new author in table author """
        self.connect()
        cur = self.con.cursor()
        cur.execute("INSERT INTO author (id, name, age, genre) VALUES (NULL, '%s','%s', '%s'); % (fname, age, genre)")
        cur.execute("commit")
        self.close()

  def find_author(self, name):
        """func find_author are looking the author in table authors,
        whose name was entered
        """
        self.connect()
        symbol = '%'
        if self.con is None:
            return []
        cur = self.con.cursor()
        cur.execute("SELECT * FROM author"
                    " WHERE name LIKE '%s';"
                    % (name))
        self.close()
        return cur.fetchall()