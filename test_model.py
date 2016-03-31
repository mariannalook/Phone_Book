#from Info import all_information
import doctest

all_information = [{'Name': 'Olga', 'Surname': 'Ivanova', 'Phone': '35746'},
                   {'Name': 'Olga', 'Surname': 'Petrov', 'Phone': '12345'},
                   {'Name': 'Alexandra', 'Surname': 'Lebedeva', 'Phone': '987'}]


def addContact(name,surname,phone):
    """
    Function adds a new contact
    :param name: contact name
    :param surname: contact surname
    :param phone:   contact phone number
    :returns : event info

    >>> addContact("Name1","Surname1","Phone1")
    'Contact with name: Name1 was added'
    """
    all_information.append({'Name':name,
                            'Surname':surname,
                            'Phone':phone})
    return "Contact with name: %s was added" %name

def getContactByName(name):
    """
    Function gets the contact by name
    :param name:
    :returns: contact.Else false

    """
    for dict in all_information:
        if dict['Name']==name:
            return dict
    else:return False

def getContactByPhone(phone):
    """
    Function gets the contact by phone
    :param phone: contact phone
    :returns: contact.Else false

    """
    for dict in all_information:
        if dict['Phone']==phone:
            return dict
    else:return False

def deleteContactByName(name):
    """
    Function deletes the contact by name
    :param name: contact name
    :returns  :event log.Else false
    >>> deleteContactByName("Name1")
    'Contact with name: Name1 was deleted'
    """

    dict = getContactByName(name)
    if dict != False:
        all_information.remove(dict)
        return "Contact with name: %s was deleted" %name
    else:return False



def deleteContactByPhone(phone):
    """
    Function deletes the contact by phone
    :param phone: contact phone
    :returns: deleted contact.Else false

    >>> addContact("Name1","Surname1","Phone1")
    'Contact with name: Name1 was added'
    >>> deleteContactByPhone("Phone1")
    'Contact with phone: Phone1 was deleted'
    """
    dict = getContactByPhone(phone)
    if dict != False:
        all_information.remove(dict)
        return "Contact with phone: %s was deleted" %phone
    else:return False

def sortByLengthOfName():
    """
    Function sorts by length of name
    :returns: event log

    >>> sortByLengthOfName()
    'List was sorted'
    """
    all_information.sort(key=lambda x: len(x["Name"]))
    return "List was sorted"

def editContact(name,newName,newSurname,newPhone):
    """
    Function edits the contact
    :param name: old contact name to edit
    :param newName: new contact name
    :param newSurname: new contact surname
    :param newPhone:  new contact phone
    :returns: event log.Else false

    >>> editContact("Olga","Name2","Surname2","Phone2")
    'Contact with name:Olga was edited'
    """
    dict = getContactByName(name)
    if dict !=False:
        dict['Name']=newName
        dict['Phone']=newPhone
        dict['Surname']=newSurname
        return "Contact with name:%s was edited" %name
    else:return False

if __name__ == '__main__':
    import doctest
    doctest.testmod()