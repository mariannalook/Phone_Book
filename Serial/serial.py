"""
Serial
"""
import pickle
import json
import yaml
from Data.data import ContactBook,Contact

class Serial:

    @staticmethod
    def encode(obj):
        tmpList=[]
        for contact in obj:
            tmpList.append({"Name":contact.name,
                            "Surname":contact.surname,
                            "Number":contact.number})
        return tmpList

    @staticmethod
    def decode(obj):
        tmpBook=ContactBook()
        for dic in obj:
            tmpContact=Contact(dic["Name"],dic["Surname"],dic["Number"])
            tmpBook.addContact(tmpContact)
        return tmpBook

    @staticmethod
    def writePickle(obj,fname='Data/info.pickle'):
        if not isinstance(obj,ContactBook):
            raise ValueError('Incorrect type of variable obj')
        with open(fname, 'wb') as file:
            pickle.dump(obj, file)

    @staticmethod
    def readPickle(fname='Data/info.pickle'):
        try:
            with open(fname, 'rb') as file:
                return pickle.load(file)
        except (OSError, ValueError):
            return None

    @staticmethod
    def writeYaml(obj, fname='Data/info.yaml'):

        if not isinstance(obj,ContactBook):
            raise ValueError('Incorrect type of variable obj')
        with open(fname, 'wt') as file:
            yaml.dump(Serial().encode(obj), file)

    @staticmethod
    def readYaml(fname='Data/info.yaml'):
        """
        read from Yaml file the object
        :param fname: file name
        :return: new list object or None
        """
        try:
            with open(fname, 'rt') as file:
                return Serial().decode(yaml.load(file))
        except (OSError, ValueError):
            return None

    @staticmethod
    def writeJson(obj, fname="Data/info.json"):

        if not isinstance(obj,ContactBook):
            raise ValueError('Incorrect type of variable obj')
        with open(fname, 'wt') as file:
            json.dump(Serial().encode(obj), file)

    @staticmethod
    def readJson(fname="Data/info.json"):
        """
        read from Json file the object
        :param fname: file name
        :return: new list object or None
        """
        try:
            with open(fname, 'rt') as file:
                return Serial().decode(json.load(file))
        except (OSError, ValueError):
            return None