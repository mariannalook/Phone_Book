from test_model import addContact, \
    deleteContactByName, deleteContactByPhone, editContact, \
    sortByLengthOfName,getContactByName,getContactByPhone
from view import showContact,showBook

def showMenu():
    return input("Enter the key:\n"
                 "1 -Add \n"
                 "2- Edit \n"
                 "3- Delete\n"
                 "4 - Sort by length\n"
                 "5 - Show book\n"
                 "6- Show contact\n"
                 "7- Exit")

def addInput():
    name=input("Enter the name:")
    surname=input("Enter the surname:")
    phone=input("Enter the phone number")
    addContact(name,surname,phone)

def editInput():
    nameToEdit=input("Enter the contact`s name to edit:")
    newName=input("Enter the new name for contact:")
    newSurname=input("Enter the new surname for contact:")
    newPhone=input("Enter the new phone number for contact:")
    editContact(nameToEdit,newName,newSurname,newPhone)

def deleteInput():
    manager=input("1 - Delete by name\n"
                  "2- Delete by phone number\n")
    if manager=='1':
        nameToDelete=input("Enter the contact`s name to delete:")
        deleteContactByName(nameToDelete)
    elif manager=='2':
        phoneToDelete=input("Enter the contact`s phone to delete:")
        deleteContactByPhone(phoneToDelete)
    else:
        print("Incorrect key pressed.")

def showInput():
    manager=input("1 - Search by name\n"
                  "2- Search by phone number\n")
    if manager=='1':
        nameToSearch=input("Enter the contact`s name to show:")
        showContact(getContactByName(nameToSearch))
    elif manager=='2':
        phoneToSearch=input("Enter the contact`s phone to show:")
        showContact(getContactByPhone(phoneToSearch))
    else:
        print("Incorrect key pressed.")

while True:
    key = showMenu()
    if key =='1':
        addInput()
    elif key=="2":
        editInput()
    elif key =="3":
        deleteInput()
    elif key=="4":
        sortByLengthOfName()
    elif key =="5":
        showBook()
    elif key =="6":
        pass
    elif key =="7":
        exit()
    else:
        print("Incorrect. Please,try again")

