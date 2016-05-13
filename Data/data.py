class Contact:
    """
    contact info class
    """

    def __init__(self, name, surname, number):
        self.name = name
        self.surname = surname
        self.number = number

    def __str__(self):
        return 'Name:{} Surname:{} Number:{}'.format(self.name, self.surname, self.number)

    def __eq__(self, other):
        if self.name == other.name and self.surname == other.surname and \
                        self.number == other.number:
            return True
        else:
            return False


class ContactBook:
    """
    contact book(container) class
    """

    def __init__(self, values=None):
        if values is None:
            self.listBook = []
        else:
            self.listBook = values

    def __getitem__(self, key):
        return self.listBook[key]

    def __delitem__(self, key):
        del self.listBook[key]

    def __setitem__(self, key, value):
        self.listBook[key] = value

    def __iter__(self):
        return iter(self.listBook)

    def addContact(self, contact):
        """
        add contact to list
        :param contact:
        :return:
        """
        self.listBook.append(contact)

    def sortByLength(self):
        """
        sort list by its length of name
        :return:
        """
        self.listBook.sort(key=lambda x: len(x.name))

    def deleteContactByName(self, name):
        """
        delete contact by name
        :param name:
        :return:
        """
        for item in self.listBook:
            if item.name == name:
                self.listBook.remove(item)
            else:
                return False

    def deleteContactByPhone(self, phone):
        """
        delete contact by number
        :param phone:
        :return:
        """
        for item in self.listBook:
            if item.phone == phone:
                self.listBook.remove(item)
            else:
                return False

    def getContactByName(self, name):
        """
        Function gets the contact by name
        :param name:
        :returns: contact.Else false

        """
        for item in self.listBook:
            if item.name == name:
                return item
        else:
            return False

    def getContactByPhone(self, phone):
        """
        Function gets the contact by phone
        :param phone: contact phone
        :returns: contact.Else false

        """
        for item in self.listBook:
            if item.phone == phone:
                return item
        else:
            return False

    def editContact(self, name, newName, newSurname, newPhone):
        """
        Function edits the contact
        :param name: old contact name to edit
        :param newName: new contact name
        :param newSurname: new contact surname
        :param newPhone:  new contact phone
        :returns: event log.Else false

        """
        item = self.getContactByName(name)
        if isinstance(item, Contact):
            item.name = newName
            item.phone = newPhone
            item.surname = newSurname
        else:
            return False

    def reload(self, values):
        """
        reload list
        :param values:
        :return:
        """
        self.listBook = values
