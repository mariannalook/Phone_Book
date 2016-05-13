"""
unit testing
"""
import unittest

from Data.data import Contact,ContactBook


class SerialTest(unittest.TestCase):
    """
    class for testing
    """
    def testContact(self):
        a=Contact("vasya","petrov","222")
        b=Contact("vasya","petrov","222")
        self.assertEqual(a,b)

    def testAddContact(self):
        a=Contact("vasya","petrov","222")
        b=ContactBook()
        b.addContact(a)
        self.assertIn(a,b.listBook)

    def testDeleteContact(self):
        a=Contact("vasya","petrov","222")
        b=ContactBook()
        b.addContact(a)
        b.deleteContactByName("vasya")
        self.assertNotIn(a,b.listBook)

    def testEditContact(self):
        a=Contact("vasya","petrov","222")
        b=ContactBook()
        b.addContact(a)
        b.editContact("vasya","petya","petrov","222")
        a=b.getContactByName("petya")
        self.assertIsInstance(a,Contact)

    def testReload(self):
        b=ContactBook()
        lst=[1,2,3]
        b.reload(lst)
        self.assertListEqual(b.listBook,lst)

if __name__ == '__main__':
    unittest.main()
