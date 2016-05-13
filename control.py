"""
controller
"""

from Model.model import Model
from Data.data import Contact, ContactBook
from View.view import View


class Control:
    @staticmethod
    def showMenu():
        """
        Main menu
        :return:
        """
        return input("Enter the key:\n"
                     "1-Add \n"
                     "2- Edit \n"
                     "3- Delete\n"
                     "4- Sort by length\n"
                     "5- Show book\n"
                     "6- Show contact\n"
                     "7- Serialization\n"
                     "8- Exit\n")

    @staticmethod
    def addInput(book):
        """
        Input for add option
        :param book:
        :return:
        """
        name = input("Enter the name:")
        surname = input("Enter the surname:")
        phone = input("Enter the phone number:")
        tmpContact = Contact(name, surname, phone)
        book.addContact(tmpContact)

    @staticmethod
    def editInput(book):
        """
        Input for edit option
        :param book:
        :return:
        """
        nameToEdit = input("Enter the contact`s name to edit:")
        newName = input("Enter the new name for contact:")
        newSurname = input("Enter the new surname for contact:")
        newPhone = input("Enter the new phone number for contact:")
        book.editContact(nameToEdit, newName, newSurname, newPhone)

    @staticmethod
    def deleteInput(book):
        """
        input for delete option
        :param book:
        :return:
        """
        manager = input("1 - Delete by name\n"
                        "2- Delete by phone number\n")
        if manager == '1':
            nameToDelete = input("Enter the contact`s name to delete:")
            book.deleteContactByName(nameToDelete)
        elif manager == '2':
            phoneToDelete = input("Enter the contact`s phone to delete:")
            book.deleteContactByPhone(phoneToDelete)
        else:
            print("Incorrect key pressed.")

    @staticmethod
    def showInput(book):
        """
        input for show option
        :param book:
        :return:
        """
        manager = input("1 - Search by name\n"
                        "2- Search by phone number\n")
        if manager == '1':
            nameToSearch = input("Enter the contact`s name to show:")
            View().showContact(book.getContactByName(nameToSearch))
        elif manager == '2':
            phoneToSearch = input("Enter the contact`s phone to show:")
            View().showContact(book.getContactByPhone(phoneToSearch))
        else:
            print("Incorrect key pressed.")

    @staticmethod
    def hideInput(book):
        """
        input for show option
        :param book:
        :return:
        """
        manager = input("1 - Search by name\n"
                        "2- Search by phone number\n")
        if manager == '1':
            nameToSearch = input("Enter the contact`s name to show:")
            View().showContact(book.getContactByName(nameToSearch))
        elif manager == '2':
            phoneToSearch = input("Enter the contact`s phone to show:")
            View().showContact(book.getContactByPhone(phoneToSearch))
        else:
            print("Incorrect key pressed.")

    @staticmethod
    def badInput(book):
        """
        Input for add option
        :param book:
        :return:
        """
        name = input("Enter the name:")
        surname = input("Enter the surname:")
        phone = input("Enter the phone number:")
        tmpContact = Contact(name, surname, phone)
        book.addContact(tmpContact)


    @staticmethod
    def feedInput(book):
        """
        Input for edit option
        :param book:
        :return:
        """
        nameToEdit = input("Enter the contact`s name to edit:")
        newName = input("Enter the new name for contact:")
        newSurname = input("Enter the new surname for contact:")
        newPhone = input("Enter the new phone number for contact:")
        book.editContact(nameToEdit, newName, newSurname, newPhone)

    @staticmethod
    def serialInput(book):
        """
        input for serialization
        :param book:
        :return:
        """

        read, write = Model().setTypeSerial()
        manager = input("1 - Load from the file\n"
                        "2 - Save to the file\n")
        if manager == "1":
            book.reload(read())
        elif manager == "2":
            write(book)
        else:
            print("Incorrect key pressed.")

    @staticmethod
    def start():
        """
        start the program
        :return:
        """
        book = ContactBook()
        while True:
            key = Control().showMenu()
            if key == '1':
                Control.addInput(book)
            elif key == "2":
                Control().editInput(book)
            elif key == "3":
                Control().deleteInput(book)
            elif key == "4":
                book.sortByLength()
            elif key == "5":
                View().showBook(book)
            elif key == "6":
                View().showContact(book)
            elif key == "7":
                Control().serialInput(book)
            elif key == "8":
                exit()
            else:
                print("Incorrect. Please,try again")


Control().start()
