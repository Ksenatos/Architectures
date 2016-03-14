"""Test"""
import unittest
#import mock
from mock import Mock
from dbClasses import Book
from dbClasses import Genre
#import sys
#sys.path.insert(0, "C:\users\Vlad\PycharmProjects\untitled\ ") путь к моделе
#import model
from model import DB
from mock import patch
from unittest.mock import create_autospec

__author__ = 'Vlad'


testdb = DB()


class TestUT(unittest.TestCase):
    """class test"""
    def test_init(self):
        """initialization"""
        self.assertIsNone(testdb.connect())

    def test_conect(self):
        """ im to tired"""
        with patch('model.DB.connect') as perm_mock:


         self.assertTrue(perm_mock('127.0.0.1', 'root', '1111', 'library'))


    def test_add_authors(self):
        """I run out of imagination to write this comments"""
        with patch('model.DB.add_author') as perm_mock:

         perm_mock('Als', 'Pehov')
         perm_mock.assert_called_once_with('Als', 'Pehov')


    def test_add_book(self):
        """I had a very long lay"""
        with patch('model.DB.add_book') as perm_mock:

         perm_mock('Straj', '1', '2')
         perm_mock.assert_called_with('Straj', '1', '2')



    def test_get_authors(self):
        """Show must go on"""
        with patch('model.DB.get_authors') as perm_mock:
         mock_function = create_autospec(perm_mock, return_value=['name', 'lname'])
         self.assertEqual(['name', 'lname'], mock_function())

    def test_get_books(self):
        """here is so many func to comment"""
        with patch('model.DB.get_books') as perm_mock:
         mock_function = create_autospec(perm_mock, return_value=['name', 'author', 'genre'])
         self.assertEqual(['name', 'author', 'genre'], mock_function())



    def test_add_genre(self):
        """AAAAAAAAAAAA_AAA__AAA"""
        with patch('model.DB.add_genre') as perm_mock:

         perm_mock('Fantasy')
         perm_mock.assert_called_with('Fantasy')

    def test_find_author(self):
        """why do we need so many functions..?"""
        with patch('model.DB.find_author') as perm_mock:

         perm_mock = Mock(return_value=None)
         perm_mock('firstAuthor')
         perm_mock('secondAuthor')
         perm_mock('thirdAuthor')
         perm_mock.assert_any_call('secondAuthor')

    def test_find_books(self):
        """i hate assembler"""
        with patch('model.DB.find_author') as perm_mock:

         perm_mock = Mock(return_value=None)
         perm_mock('firstBook')
         perm_mock('secondBook')
         perm_mock('thirdBook')
         perm_mock.assert_any_call('thirdBook')

    def test_delete_book(self):
        """YYUUPA! the last one!"""
        with patch('model.DB.find_author') as perm_mock:

         perm_mock = Mock(return_value=None)
         perm_mock('firstBook')
         perm_mock('secondBook')
         perm_mock('thirdBook')
         perm_mock.assert_any_call('secondBook')





if __name__ == '__main__':
    unittest.main()



