"""
Model
"""
import configparser
from Serial.serial import Serial


class Model:
    """
    model class
    """

    @staticmethod
    def setTypeSerial(fname="Data/defaults.cfg"):
        """
        choose type of serialization
        :param fname: configure file name
        :return: functions read/write
        """
        # get configure file
        parser = configparser.ConfigParser()
        parser.read(fname)
        # get type of serialization
        serialType = parser['serialization']['type']
        if serialType == 'json':
            # JSON
            return Serial().readJson, Serial().writeJson
        elif serialType == 'pickle':
            # pickle
            return Serial().readPickle, Serial().writePickle
        elif serialType == 'yaml':
            # YAML
            return Serial().readYaml, Serial().writeYaml
        else:
            # unknown type
            raise AttributeError('Incorrect serialization type')
