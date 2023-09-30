import unittest
import json
import os
import sys

# Get the path of "Backend" directory so that we can import the necessary file 
dir = os.path.dirname(os.path.realpath("../Backend"))
sys.path.append(dir)

import sortSingles
from unittest.mock import patch 



class sortSinglesTest(unittest.TestCase):

    # Set up Class, this runs once before all tests start
    @classmethod
    def setUpClass(cls):
        # Opening the test json file -> From Jack
        cls.testFile = open('../Backend/json/test.json') # Might have to change this depending on your directory 
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

    # For this test case function we need to use a special function called mock from the unittest
    # framework. Here patch creates a "sample" object that mimics the weightRoom function.
    # This is because idealSearch depends on the results of weightRoom. 
    @patch('sortSingles.weightRoom') 
    def test_idealSeach(self, mock_weightRoom):
        
        print("Testing ideal search function")
        
        # Thanks to mock, we can modify the return value of weightroom
        mock_weightRoom.return_value = 6
        mock_weightRoom.student = self.student

        # Giving a sample potential rooms for the function to use
        sampleRooms = [
        { "Warren1-8": {
            "name": "Warren",
            "sex": "m",
            "size": 2,
            "shared_bathroom": False,
            "year": "freshman",
            "occupants": [
                {
                    "name": "William",
                    "sex": "m",
                    "major": "Computer Science",
                    "dormPref": "",
                    "year": "freshman",
                    "geo": "NJ",
                    "sleepHours": [
                        9,
                        7
                    ],
                    "musicPreference": [
                        "Classical",
                        "Rock"
                    ],
                    "hobbies": [
                        "Instrument"
                    ],
                    "dorm": "Warren"
                }
            ],
            "ra room": False
        }   
        },
        {
            "Warren1-16": {
            "name": "Warren",
            "sex": "m",
            "size": 1,
            "shared_bathroom": False,
            "year": "freshman",
            "occupants": [],
            "ra room": True
            }
        }
        ]
        
        sortSingles.potentialRooms.append(sampleRooms)
        
        # See if student is placed in the correct spot
        expectedOccupants = self.dataTestFile["Warren1-8"]["occupants"]
        expectedOccupants.append(self.student)

        
        # Call the function     
        sortSingles.idealSearch(self.student)
        
        self.assertEqual(expectedOccupants, self.dataTestFile["Warren1-8"]["occupants"])


    def test_isPerfectMatch(self):
        self.assertEqual(1 , 1)

    def test_firstSerach(self):
        self.assertEqual(1 , 1)

    # ----------------------------------------------------------------------------------
    # Tear down class, this runs once after all tests are over
    @classmethod
    def tearDownClass(cls):
        cls.testFile.close() # Close test file that was opened by setupclass


if __name__ == '__main__':

    unittest.main()
