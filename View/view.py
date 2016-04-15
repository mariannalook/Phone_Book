
def showBook(book):
    """
    This function shows
    :param book:
    :return:
    """
    for contact in book:
        print("Name:", contact['Name'], ";",
              "Last Name:", contact['Surname'], ";",
              "Phone Number:", contact["Phone"])


def showContact(contact):
    """
    This function shows contact
    :param contact:
    :return:
    """
    if contact:
        print("Name:", contact['Name'], ";",
              "Last Name:", contact['Surname'], ";",
              "Phone Number:", contact["Phone"])
