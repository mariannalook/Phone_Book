"""
pickle module to serialize
"""

import pickle


def write(obj, fname='Data/info.pickle'):
    """
    serialize user object in Pickle file
    :param obj: list with information to serialize
    :param fname: file name
    :return: nothing
    """
    if type(obj) != list:
        raise ValueError('Incorrect type of variable obj')
    with open(fname, 'wb') as file:
        pickle.dump(obj, file)


def read(fname='Data/info.pickle'):
    """
    read from Pickle file the object
    :param fname: file name
    :return: new list object or None
    """
    try:
        with open(fname, 'rb') as file:
            return pickle.load(file)
    except (OSError, ValueError):
        return None
