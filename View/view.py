def showBook(obj):
    """
    This function shows our book
    :return:
    """
    for contact in obj:
        print("Name:", contact['Name'], ";",
              "Last Name:", contact['Surname'], ";",
              "Phone Number:", contact["Phone"])


def showContact(contact):
    """
    This function shows
    our contact
    :param contact:
    :return:
    """
    if contact:
        print("Name:", contact['Name'], ";",
              "Last Name:", contact['Surname'], ";",
              "Phone Number:", contact["Phone"])
