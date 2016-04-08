"""
json module to serialize
"""

import json


def write(obj, fname="Data/info.json"):
    """
    Serialize user object in Json file
    :param obj: list with information to serialize
    :param fname: file name
    :return:
    """
    if type(obj) != list:
        raise ValueError('Incorrect type of variable obj')
    with open(fname, 'wt') as file:
        json.dump(obj, file)


def read(fname="Data/info.json"):
    """
    read from Json file the object
    :param fname: file name
    :return: new list object or None
    """
    try:
        with open(fname, 'rt') as file:
            return json.load(file)
    except (OSError, ValueError):
        return None
