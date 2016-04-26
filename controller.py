"""controller module"""
from model import DB
from view import View
import configparser
# import coverage

__author__ = 'paul'
'''Using config to choose the serialization type'''
try:
    config = configparser.ConfigParser()
    config.read('files/config.py')
except configparser.ParsingError:
    print('could not parse')
try:
    option = config.get('ModelFile', 'ModelType')
except:
    print("exception on %s!" % option)

if option == 'pickle':
    from serialPickle import serialization
    from serialPickle import deserialization
elif option == 'json':
    from serialJSON import serialization
    from serialJSON import deserialization
elif option == 'yaml':
    from serialYaml import serialization
    from serialYaml import deserialization
else:
    print('<files/config.py>% wrong option')





if __name__ == "__main__":
    Controller().run()
