#   _   _   _   _   _   _   _   _   _   _  
#  / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ 
# ( H | o | u | s | i | n | g | 2 | . | 0 )
#  \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ 
#

# Author: Daniel 
#
# Description:
# Purpose of this code is to create a json file that contains all rooms in crockett hall
# This Json file will be filled in with RANDOM students at random locations
# This resulting file can be then passed into the database for testing search algorithms
#
# Limitations: 
# - Can not accurately generate Crockett hall
# - Can only generate one floor of Crockett
# - Assumes all rooms are of size 2 

import random
import json
import time

# First grabbing some json ... 
# Replace with your own path! 
with open('/home/beef-patty/Desktop/Housing2.0_Fall_2023/Housing-2.0/Backend/json/hobbies.json') as f:
    hobbies = json.load(f) # A list of hobbies 

with open('/home/beef-patty/Desktop/Housing2.0_Fall_2023/Housing-2.0/Backend/json/music.json') as f:
    music = json.load(f) # A list of music genres

with open('/home/beef-patty/Desktop/Housing2.0_Fall_2023/Housing-2.0/Backend/json/names.json') as f:
    names = json.load(f) # A list of names

with open('/home/beef-patty/Desktop/Housing2.0_Fall_2023/Housing-2.0/Backend/json/states.json') as f:
    states = json.load(f) # A list of states 

with open('/home/beef-patty/Desktop/Housing2.0_Fall_2023/Housing-2.0/Backend/json/majors.json') as f:
    majors = json.load(f) # A list of majors


# Function to loop 0 - N times, running a function 'func' and returning a list
# of results
def return_random_list(func, list: list, maxIter: int) -> list:
    
    resultList = []
    amILooping = random.choice([True, False])
    
    if amILooping: 
        iterations = random.randint(1, maxIter)

        for i in range(iterations):
            resultList.append( func(list) )
    return resultList
    

# Function to return a random element in a list
def pick_from_list(list: list) -> str:
    randomIndex = random.randint(0, len(list) - 1)
    return list[randomIndex]

# Function to generate a random student
# A student is defined as such: 
# name, sex, major, dormPref, year, geo, sleepHours, musicPreference, hobbies, dorm

def random_student(sex: str) -> dict:
    resultDict = {}
    resultDict['name'] = pick_from_list(names)
    resultDict['sex'] = sex
    resultDict['major'] = pick_from_list(majors)
    resultDict['dormPref'] = ""
    resultDict['year'] = "freshman"
    resultDict['geo'] = pick_from_list(states)
    resultDict['sleepHours'] = generate_sleep_schedule()
    resultDict['musicPreference'] = return_random_list(pick_from_list, music, 10)
    resultDict['hobbies']  = return_random_list(pick_from_list, hobbies, 4) 
    resultDict['dorm'] = 'Crockett'

    return resultDict

# Call random_student N times
def generate_n_students(N: int) -> list:
    resultList = []
    for i in range(1, N):
        resultList.append( random_student("m") )
    
    return resultList

# Generate a student's sleep schedule 
def generate_sleep_schedule() -> list:
    resultList = []
    bedTime = random.randint(8, 12) # Hypothetical sleep time of 8PM -> 12AM  
    wakeupTime = random.randint(5, 10) # Hypothetical wake up time of 5AM -> 10AM 

    resultList.append(bedTime)
    resultList.append(wakeupTime)

    return resultList

# Function to generate crockett ... 
# For now the function can only generate the first floor due to lack of information 
def generate_dorm() -> dict: 
    resultDict = {}

    # Let's say that there are 20 rooms on the first floor ... 
    for i in range(1, 20):
        new_room = generate_room(1, i + 100, 2, "m", False)
        resultDict.update(new_room)

    return resultDict

# Helper function to generate room 
def generate_room(floor: int, roomNum: int, size: int, sex: str, shared_bathroom: bool) -> dict:
    roomName = "Crockett" + str(floor) + "-" + str(roomNum) 
    resultDict = {roomName: {}}
    resultDict[roomName]["name"] = "Crockett"
    resultDict[roomName]["sex"] = sex
    resultDict[roomName]["size"] = size
    resultDict[roomName]["shared_bathroom"] = shared_bathroom
    resultDict[roomName]["year"] = "freshman"
    resultDict[roomName]["occupants"] = []
    return resultDict

# Given a dorm and students, populate the dorm with students, return True on success
def populate(dorm: dict, students: list) -> bool: 
    
    students_index = 0
    num_students = len(students)

    while students_index < num_students: 
        # Pick a random room: 
        random_room = random.choice( list(dorm.keys()) )
        # Check if room is full
        if len(dorm[random_room]["occupants"]) < dorm[random_room]["size"]:
            # If not, put student inside, increment index
            dorm[random_room]["occupants"].append(students[students_index])
            students_index += 1
        else: 
            # Else go to next room 
            continue; 
    
    return True; 

if __name__ == "__main__": 

    print("Generating Crockett Dorm .... ")

    crockett = generate_dorm()

    print("Done!")

    print("Generating Students ...")

    # Generating 29 students
    
    students = generate_n_students(29)

    print("Done!")

    print("Populating Dorm ... ")

    populateResult = populate(crockett, students)

    if populateResult == True: 
        print("Done!")
    else: 
        print("Error in populating ... ")
        exit

    time.sleep(1)

    print("Complete!")

    print("Writing to json ... ")

    # Serializing json
    json_object = json.dumps(crockett, indent=4)
 
    # Writing to sample.json
    with open("crockett.json", "w") as outfile:
        outfile.write(json_object)
    outfile.close()

    f.close()
