"""
yaml module to serialize
"""

import yaml


def write(obj, fname='Data/info.yaml'):
    """
    serialize user object in Yaml file
    :param obj: list with information to serialize
    :param fname: file name
    :return: nothing
    """
    if type(obj) != list:
        raise ValueError('Incorrect type of variable obj')
    with open(fname, 'wt') as file:
        yaml.dump(obj, file)


def read(fname='Data/info.yaml'):
    """
    read from Yaml file the object
    :param fname: file name
    :return: new list object or None
    """
    try:
        with open(fname, 'rt') as file:
            return yaml.load(file)
    except (OSError, ValueError):
        return None
