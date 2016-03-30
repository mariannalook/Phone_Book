from model import all_information

def showBook():
    for contact in all_information:
        print("Name:", contact['Name'], ";",
              "Last Name:", contact['Surname'], ";",
              "Phone Number:", contact["Phone"])


def showContact(contact):
        print("Name:", contact['Name'], ";",
            "Last Name:", contact['Surname'], ";",
            "Phone Number:", contact["Phone"])






