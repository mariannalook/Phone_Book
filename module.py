#list of entities
contactBook = []

def addContact(name,phoneNumber,email):
    contactEntity  = {}
    contactEntity["name"] = name
    contactEntity["phoneNumber"] = phoneNumber
    contactEntity["email"] = email
    contactBook.__add__(contactEntity)

def removeContact(name):
    for contact in contactBook:
        if contact["name"] == name:
            print("Contact with name "+name+" was deleted")
            contactBook.remove(contact)
            return
    else:
        print ("Contact with name "+name+ " was not found")


