#   _   _   _   _   _   _   _   _   _   _  
#  / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ 
# ( H | o | u | s | i | n | g | 2 | . | 0 )
#  \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ 
#

# Original Author: Daniel He 
# This python file here is a testing file used to test sortSingles.py
# I've set up tests in a way where anyone can run the same tests and tried to
# make it as flexible as possible where anyone can create their own test cases
# to test. I would highly recommend using VSCode for these tests as it has 
# support for python unittest 

# October 3rd, 2023 status - Daniel
# Improvements need to be done with the test cases, currently they are too small scale.
# However overall, base line test cases are finished. 
# Next goal should be adding more realistic and detailed cases as well as edge cases

import unittest
import json
import os
import sys

# Get the path of "Backend" directory so that we can import the necessary file 
dir = os.path.dirname(os.path.realpath("../Backend"))
sys.path.append(dir)

import sortSingles
from unittest.mock import patch 

# Here is were all the testing begins 
class sortSinglesTest(unittest.TestCase):
    
    # Set up Class, this runs once before all tests start, it's essentially creating
    # attributes that all other test fuctions can access 
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
    # Set up and tear down functions. Set up runs before each test case. 
    # These do nothing for now. 
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
    # This is because idealSearch depends on the results of weightRoom. If we don't create this 
    # object it can cause an error where test_WeightRoom runs fails. [ Get rid of patch to see 
    # what I mean ;) ]
    @patch('sortSingles.weightRoom') 
    def test_idealSeach(self, mock_weightRoom):

        # Giving a sample potential rooms for the function to use
        sampleRooms = [
        {
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
             
        },
        {
            "name": "Warren",
            "sex": "m",
            "size": 1,
            "shared_bathroom": False,
            "year": "freshman",
            "occupants": [],
            "ra room": True
        }
        ]

        print(sampleRooms[0])

        # Thanks to mock, we can modify the return value of weightroom
        mock_weightRoom.return_value = 6
        mock_weightRoom.student = self.student

        # Fill in potential rooms since it is being used by idealSearch :p
        for i in range(0, len(sampleRooms)):
            sortSingles.potentialRooms.append(sampleRooms[0])

        # Where the student is expected to go
        expectedOccupants = self.dataTestFile["Warren1-8"]["occupants"]
        expectedOccupants.append(self.student)
        
        # Call the function, store into result to be used for comparison later    
        result = sortSingles.idealSearch(self.student)
        
        # See if student is placed in the correct spot
        self.assertEqual(expectedOccupants, result["occupants"] )

    
    def test_isPerfectMatch(self):

        room = self.dataTestFile["Warren1-8"]

        result = sortSingles.isPerfectMatch( room, self.student )

        # Perfect match should return true with current room
        self.assertEqual(True, result)

        # Next test, Test with room that doesn't match

    # Test 
    def test_firstSerach(self): 
        
        result = sortSingles.firstSearch( self.dataTestFile, self.student) 
        # firstSearch should return true using current all available rooms 
        self.assertEqual(True, result)

        # Now what happens when all rooms are full? .... 
        # Is the student being placed where we expect him to be? ... 

    # ----------------------------------------------------------------------------------
    # Tear down class, this runs once after all tests are over
    @classmethod
    def tearDownClass(cls):
        cls.testFile.close() # Close test file that was opened by setupclass

# Call unittest in main
if __name__ == '__main__':

    unittest.main()
