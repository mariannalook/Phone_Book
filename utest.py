"""
unit testing
"""
import unittest
import yaml
import json
import pickle


class SerialTest(unittest.TestCase):
    """
    class for testing
    """

    def testYaml(self):
        """
        test yaml serialization
        :return: nothing
        """
        testInfo = [{"Name": "TestName", "Surname": "TestSurname",
                     "Phone": "TestPhone"}]

        stringIO = yaml.dump(testInfo)
        testInfo2 = yaml.load(stringIO)
        self.assertEquals(testInfo, testInfo2)

    def testJSON(self):
        """
        test JSON serialization
        :return: nothing
        """
        testInfo = [{"Name": "TestName", "Surname": "TestSurname",
                     "Phone": "TestPhone"}]

        stringIO = json.dumps(testInfo)
        testInfo2 = json.loads(stringIO)
        self.assertEquals(testInfo, testInfo2)

    def testPickle(self):
        """
        test Pickle serialization
        :return: nothing
        """
        testInfo = [{"Name": "TestName", "Surname": "TestSurname",
                     "Phone": "TestPhone"}]

        stringIO = pickle.dumps(testInfo)
        testInfo2 = pickle.loads(stringIO)
        self.assertEquals(testInfo, testInfo2)


if __name__ == '__main__':
    unittest.main()
