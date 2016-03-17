# list of entities
contactBook = []


def showBook(book):
    for contact in book:
        print("Name:",contact['name'],";",
              "Last Name:",contact['lastName'],";",
              "Phone Number:",contact["number"])

def showContact(name,book):
    for contact in book:
        if contact["name"] ==name:
            print("Name:",contact['name'],";",
              "Last Name:",contact['lastName'],";",
              "Phone Number:",contact["number"])
            return
    else:
        print("Contact with name " + name + " was not found.")




contactBook = [{"name":"vasya","lastName":"Grek","number":"245"},
               {"name":"Roma","lastName":"Luk","number":"222"},
               {"name":"Victor","lastName":"Agnastasiev","number":"977"}]



contactBook.sort(key= lambda x: len(x["lastName"]))
showBook(contactBook)
showContact("Roma",contactBook)



