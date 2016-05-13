"""
View
"""
from Data.data import Contact,ContactBook

class View:
    @staticmethod
    def showBook(obj):
        """
        This function shows book
        :param obj:
        :return:
        """
        if isinstance(obj,ContactBook):
            for contact in obj:
                print(contact)
        else:
            raise ValueError('Incorrect type of variable obj')
    @staticmethod
    def showContact(item):
        """
        This function shows contact
        :param item:
        :return:
        """
        if isinstance(item,Contact):
            print(item)









