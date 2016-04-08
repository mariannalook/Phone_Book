"""
XML serialize
"""

from xml.etree.ElementTree import Element, SubElement
from xml.etree import ElementTree
from xml.dom import minidom


def createXML(obj):
    """
    creates a xml file with data
    :param obj:
    :return:
    """
    top = Element('all_information')
    for contact in obj:
        xml_contact = SubElement(top, "contact")
        xml_contact.set("Name", contact['Name'])
        xml_contact.set("Surname", contact["Surname"])
        xml_contact.set("Phone", contact["Phone"])
    return top


def prettifyXML(elem):
    """
    Return a pretty-printed XML string for the Element.
    :param elem: XML top
    :return: pretty-printed XML
    """
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="\t")


def parseXML(tree):
    """
    try to parse XML from tree
    :param tree: XML
    :return: list
    """
    # get root
    root = tree.getroot()
    info = []

    for contact in root:
        info.append({'Name': contact.attrib["Name"],
                     'Surname': contact.attrib["Surname"],
                     'Phone': contact.attrib["Phone"]})
    return info


def write(obj, fname='Data/info.xml'):
    """
    serialize user object in XML
    :param obj: class User to serialize
    :param fname: file name
    :return: nothing
    """
    if type(obj) != list:
        raise ValueError('Incorrect type of variable obj')
    with open(fname, "wt") as file:
        file.write(prettifyXML(createXML(obj)))


def read(fname='Data/info.xml'):
    """
    deserialize user object in XML
    :param fname: file name
    :return: class User
    """
    try:
        return parseXML(ElementTree.parse(fname))
    except (OSError, ValueError):
        return None
