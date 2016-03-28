from io import StringIO
import unittest
from model import DB
import serialJSON
import serialPickle

#f1 = open('files/basic.json')
#s1 = f1.read()

#print(s1)

serialJSON.makeJSONSerialize()
f1 = open('files/basic.json')
s1 = f1.read()
f = StringIO(s1)
s2 = f.getvalue()
#print (s2)

class TestSer(unittest.TestCase):

  def test_SerJason(self):
   serialJSON.makeJSONSerialize()
   f1 = open('files/basic.json')
   s1 = f1.read()
   f = StringIO(s1)
   s2 = f.getvalue()
   #print (s2)
   self.assertEqual(s2, s1)

  def test_PickSer(self):
   serialPickle.makePickleSerialization()
   f1 = open('files/data.pickle')
   s1 = f1.read()
   f = StringIO(s1)
   s2 = f.getvalue()
   #print (s2)
   self.assertEqual(s2, s1)

  def test_JsonDes(self):
    # put your author for correct test
    self.assertIn([{'Lname': 'Pupkin', 'id_author': 1, 'Fname': 'Ivan'}], serialJSON.getJSONDeserialize())

  def test_PickDes(self):
      stroka = str(serialPickle.getPickleDeserialize())
      f = StringIO(stroka)
      self.assertEqual(0, f.tell())
      f.seek(0,1)
      self.assertIsNot(f.read(5), f.read(5))

if __name__ == '__main__':
 unittest.main()
