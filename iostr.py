from io import StringIO
import unittest
import serialJSON
import serialPickle
import serialYaml



class TestSer(unittest.TestCase):

  def test_SerJason(self):
   """test function for Json serial """
   serialJSON.serialization
   f1 = open('files/basic.json')
   s1 = f1.read()
   f = StringIO(s1)
   s2 = f.getvalue()
   #print (s2)
   self.assertEqual(s2, s1)
   f.close()

  def test_PickSer(self):
   """test function for pickle serial """
   serialPickle.serialization
   f1 = open('files/data.pickle','rb')
   s1 = str(f1.read())
   f = StringIO(s1)
   s2 = f.getvalue()
   #print (s2)
   self.assertEqual(s2, s1)
   f.close()

  def test_JsonDes(self):
    """test function for Json deserial """
    s1= str(serialJSON.deserialization)
    f = StringIO(s1)
    s2 = f.getvalue()
    self.assertRaisesRegex(ValueError, 'Always different adress')
    #self.assertIn({"g.name": "drama", "lname": "Stark", "name": "Hamlet", "fname": "Tony"}, serialJSON.deserialization)
    f.close()

  def test_PickDes(self):
      """test function for pick deserial """
      stroka = str(serialPickle.deserialization)
      f = StringIO(stroka)
      self.assertEqual(0, f.tell())
      f.seek(0,1)
      self.assertIsNot(f.read(5), f.read(5))
      f.close()


  def test_SerYaml(self):
   """test function for yamal serial """
   serialYaml.serialization
   f1 = open('files/data.yml')
   s1 = f1.read()
   f = StringIO(s1)
   s2 = f.getvalue()
   #print (s2)
   self.assertEqual(s2, s1)
   f.close()

  def test_YamlDes(self):
    """test function for yamal deserial """
    s1= str(serialYaml.deserialization)
    f = StringIO(s1)
    s2 = f.getvalue()
    self.assertRaisesRegex(ValueError, 'Always different adress')
    f.close()

if __name__ == '__main__':
 unittest.main()
