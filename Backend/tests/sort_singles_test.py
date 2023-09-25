import unittest
import json
import os
import sys

# Get the path of "Backend" directory so that we can import the necessary file 
dir = os.path.dirname(os.path.realpath("../Backend"))
sys.path.append(dir)

import sortSingles 

class sortSinglesTest(unittest.TestCase):

    # Set up Class, this runs once before all tests start
    @classmethod
    def setUpClass(cls):
        # Opening the test json file -> From Jack
        cls.testFile = open('../json/test.json')
        cls.dataTestFile = json.load(cls.testFile)
        # Setting up student, This student is a freshman looking for a dorm 
        cls.student = {
            "name": "Reagan",
            "sex": "m",
            "major": "Computer Science",
            "dormPref": "",
            "year": "freshman",
            "geo": "NY",
            "sleepHours": [11, 7],
            "musicPreference": [],
            "hobbies": [],
            "dorm": ""
        }

    # ----------------------------------------------------------------------------------
    # Set up and tear down functions. Set up runs before each test case
    def setUp(self):
        pass

    def tearDown(self):
        pass 

    # ----------------------------------------------------------------------------------
    # Test Cases
    def test_weightRoom(self):
        print("Testing weight Room function")

        # Let's grab a room from the test json and see if it returns the correct weight 
        room = self.dataTestFile["Warren1-8"]
        testWeight = sortSingles.weightRoom(room, self.student)

        # Based on the estimate the student should have an actual weight of 6 once
        # this algorithm runs
        actualWeight = 6
        
        self.assertEqual(actualWeight, testWeight)

    def test_idealSeach(self):
        self.assertEqual(1 , 1)

    def test_isPerfectMatch(self):
        self.assertEqual(1 , 1)

    def test_firstSerach(self):
        self.assertEqual(1 , 1)

    # ----------------------------------------------------------------------------------
    # Tear down class, this runs once after all tests are over
    @classmethod
    def tearDownClass(cls):
        cls.testFile.close()


if __name__ == '__main__':

    unittest.main()
