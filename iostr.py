from io import StringIO
import unittest
import serialJSON
import serialPickle
import serialYaml



class TestSer(unittest.TestCase):

  def test_SerJason(self):
   serialJSON.serialization
   f1 = open('files/basic.json')
   s1 = f1.read()
   f = StringIO(s1)
   s2 = f.getvalue()
   #print (s2)
   self.assertEqual(s2, s1)
   f.close()

  def test_PickSer(self):
   serialPickle.serialization
   f1 = open('files/data.pickle')
   s1 = f1.read()
   f = StringIO(s1)
   s2 = f.getvalue()
   #print (s2)
   self.assertEqual(s2, s1)
   f.close()

  def test_JsonDes(self):
    s1= str(serialJSON.deserialization)
    f = StringIO(s1)
    s2 = f.getvalue()
    self.assertRaisesRegex(ValueError, 'Always different adress')
    #self.assertIn({"g.name": "drama", "lname": "Stark", "name": "Hamlet", "fname": "Tony"}, serialJSON.deserialization)
    f.close()

  def test_PickDes(self):
      stroka = str(serialPickle.deserialization)
      f = StringIO(stroka)
      self.assertEqual(0, f.tell())
      f.seek(0,1)
      self.assertIsNot(f.read(5), f.read(5))
      f.close()


  def test_SerYaml(self):
   serialYaml.serialization
   f1 = open('files/data.yml')
   s1 = f1.read()
   f = StringIO(s1)
   s2 = f.getvalue()
   #print (s2)
   self.assertEqual(s2, s1)
   f.close()

  def test_YamlDes(self):
    s1= str(serialYaml.deserialization)
    f = StringIO(s1)
    s2 = f.getvalue()
    self.assertRaisesRegex(ValueError, 'Always different adress')
    f.close()

if __name__ == '__main__':
 unittest.main()
