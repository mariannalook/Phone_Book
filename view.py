from test_model import all_information

def showBook():
    """
    This function shows book
    :return:
    """
    for contact in all_information:
        print("Name:", contact['Name'], ";",
              "Last Name:", contact['Surname'], ";",
              "Phone Number:", contact["Phone"])


def showContact(contact):
    """
    This function shows contact
    :param contact:
    :return:
    """
    if contact !=False:
        print("Name:", contact['Name'], ";",
            "Last Name:", contact['Surname'], ";",
            "Phone Number:", contact["Phone"])






