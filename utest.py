"""
unit testing
"""
import unittest
import unittest.mock as mock

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
        b=ContactBook()
        with mock.patch("Data.data.Contact")as mk:
            instance = mk.return_value
            instance.name="vasya"
            instance.surname="petrov"
            instance.number="222"
            b.addContact(instance)
            self.assertIn(instance,b.listBook)

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
