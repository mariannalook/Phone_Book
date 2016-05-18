from console import Console
from control import Control
import  configparser


def setTypeControl(fname="Data/defaults.cfg"):
    """
    choose type of controller
    :param fname:
    :return:
    """
    parser = configparser.ConfigParser()
    parser.read(fname)
    controlType = parser['controller']['type']
    if controlType == "default":
        return Control().start
    elif controlType == "console":
        return Console().readConsole
    else:
        raise AttributeError('Incorrect controller type')


start = setTypeControl()
start()
