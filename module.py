
def showBook(book):
    for contact in book:
        print("Name:", contact['Name'], ";",
              "Last Name:", contact['Sername'], ";",
              "Phone Number:", contact["Phone"])


def showContact(name, book):
    for contact in book:
        if contact["Name"] == name:
            print("Name:", contact['Name'], ";",
                  "Last Name:", contact['Sername'], ";",
                  "Phone Number:", contact["Phone"])
            return
    else:
        print("Contact with name " + name + " was not found.")



#contactBook.sort(key=lambda x: len(x["Sername"]))
#showBook(contactBook)
#showContact("Roma", contactBook)

