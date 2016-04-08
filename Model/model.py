import configparser
import Serial.spickle as spickle
import Serial.sjson as sjson
import Serial.syaml as syaml
import Serial.sxml as sxml

all_information = [{'Name': 'Olga', 'Surname': 'Ivanova', 'Phone': '35746'},
                   {'Name': 'Olga', 'Surname': 'Petrov', 'Phone': '12345'},
                   {'Name': 'Alexandra', 'Surname': 'Lebedeva', 'Phone': '987'}]


def addContact(name, surname, phone):
    """
    Function adds a new contact
    :param name: contact name
    :param surname: contact surname
    :param phone:   contact phone number
    :returns : event info

    >>> addContact("Name1","Surname1","Phone1")
    'Contact with name: Name1 was added'
    """
    all_information.append({'Name': name,
                            'Surname': surname,
                            'Phone': phone})
    return "Contact with name: %s was added" % name


def getContactByName(name):
    """
    Function gets the contact by name
    :param name:
    :returns: contact.Else false

    """
    for dict in all_information:
        if dict['Name'] == name:
            return dict
    else:
        return False


def getContactByPhone(phone):
    """
    Function gets the contact by phone
    :param phone: contact phone
    :returns: contact.Else false

    """
    for dict in all_information:
        if dict['Phone'] == phone:
            return dict
    else:
        return False


def deleteContactByName(name):
    """
    Function deletes the contact by name
    :param name: contact name
    :returns  :event log.Else false
    >>> deleteContactByName("Name1")
    'Contact with name: Name1 was deleted'
    """

    dict = getContactByName(name)
    if dict:
        all_information.remove(dict)
        return "Contact with name: %s was deleted" % name
    else:
        return False


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
    if dict:
        all_information.remove(dict)
        return "Contact with phone: %s was deleted" % phone
    else:
        return False


def sortByLengthOfName():
    """
    Function sorts by length of name
    :returns: event log

    >>> sortByLengthOfName()
    'List was sorted'
    """
    all_information.sort(key=lambda x: len(x["Name"]))
    return "List was sorted"


def editContact(name, newName, newSurname, newPhone):
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
    if dict:
        dict['Name'] = newName
        dict['Phone'] = newPhone
        dict['Surname'] = newSurname
        return "Contact with name:%s was edited" % name
    else:
        return False


def setTypeSerial(fname="Data/defaults.cfg"):
    """
    choose type of serialization
    :param fname: configure file name
    :return: functions read/write
    """
    # get configure file
    parser = configparser.ConfigParser()
    parser.read(fname)
    # get type of serialization
    serialType = parser['serialization']['type']
    if serialType == 'json':
        # JSON
        return sjson.read, sjson.write
    elif serialType == 'xml':
        # XML
        return sxml.read, sxml.write
    elif serialType == 'pickle':
        # pickle
        return spickle.read, spickle.write
    elif serialType == 'yaml':
        # YAML
        return syaml.read, syaml.write
    else:
        # unknown type
        raise AttributeError('Incorrect serialization type')


def setNewInfo(obj):
    """
    set the new data
    :param obj: loaded data
    :return:
    """
    global all_information
    all_information = obj


def getData():
    """
    get the main data list
    :return: list
    """
    return all_information


if __name__ == '__main__':
    import doctest

    doctest.testmod()
