#   _   _   _   _   _   _   _   _   _   _  
#  / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ 
# ( H | o | u | s | i | n | g | 2 | . | 0 )
#  \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ 
#
 
# Original Author: Jack Sherick
# What I maybe plan to do is that if there are no "perfect" matches,
# collect rooms that are good matches and sort between those and pick
# the best of them - this sort of emulates a best fit and ideal fit at
# the same time (will be two seperate sort functions *if a perfect fit
# is not found*)

# I want to have it working with just individual students before I implement
# groups - though that shouldn't be hard since groups will pretty much always
# fit under the perfect fit category of things

# September 19th, 2023 Changes - Daniel He 
# - Going to review/ modify code written by Jack adding comments 
# September 22th, 2023 Changes - Daniel he
# - I believe documentation is almost finished, starting tests right now 

# -----------------------------------------------------------------------------------------
# Helper function - Daniel 
# Checking to see if an attribute for a student exists by calling the isinstance and checking 
# the data type to determine if the attribute exists -- Requires testing
def checkAttribute (student, attri): 

    if(isinstance(student[attri], list) and len(student[attri]) == 0):
        return False
    if(isinstance(student[attri], str) and len(student[attri]) == 0):
        return False
    if(isinstance(student[attri], int) and student[attri] == 0):
        return False
    # Attribute Exists return True
    return True

# -----------------------------------------------------------------------------------------

# Start of ideal Search 

potentialRooms = [] # Houses potential rooms for the student

# Function: weightRoom()
# Description: Weighs a room based  on a bunch of variables - to change, currently acts as just an example 
# of what it will be, function is very flexible and can always add more comparisons. Helper for ideal search 
# Parameters: Takes in room information as well as stuent information
# Returns: Weight calculated 

def weightRoom(room, currStudent):

    # Holds room weight 
    weight = 0

    # Searches through occupants calculating weight based on a variety of factors
    # aStudent represents a occupant in the room 
    for aStudent in room["occupants"]:
        # Compare majors
        weight += 5 if (aStudent["major"] == currStudent["major"]) else 0
        
        # Compare geography (aka where they are from )
        weight += 3 if (aStudent["geo"] == currStudent["geo"]) else 0
        
        # Compare sleep hours, this is stored as a array where the sleep hours of a student looks like this:
        #
        # [ (Start Bedtime), (End Bedtime) ]
        #         0              1           
        #
        for sleepIndex in range(2):
            if (aStudent["sleepHours"][sleepIndex] == currStudent["sleepHours"][sleepIndex] or 
                aStudent["sleepHours"][sleepIndex] + 1 == currStudent["sleepHours"] or 
                aStudent["sleepHours"][sleepIndex] - 1 == currStudent["sleepHours"]):
                weight += 1
                

        # Compare music preference between the two students
        for musicPref in aStudent["musicPreference"]:
            weight += 1 if (musicPref in currStudent["musicPreference"]) else 0
            

        # Compare hobbies between the two students
        for hobby in aStudent["hobbies"]:
            weight += 1 if (hobby in currStudent["hobbies"]) else 0

    # If there is no one in the room we increase the weight
    if (weight == 0 and len(room["occupants"]) == 0):
        weight += 1

    # Increase the weight if the room is in a dorm of a student's preference
    
    weight += 5 if (room["name"] in currStudent["dormPref"]) else 0

    # Jacks original code for calculating weight if dorm room is a student's preference
    # k = 0
    # for dorm in currStudent["dormPref"]:
    #     if (dorm == room["name"]):
    #         weight += 5 - k
    #         k += 1

    # Return calculated weight
    return weight

# Function: idealSearch ()
# Description: Places a student into a potential room based on calculated weight of the
# room. 
# NOTE: for now the database is not modified, idealSearch returns a bestMatch instead for testing purposes
# Parameters: student
# Returns: bestMatch 

# After first search, uses potentialRooms to look
def idealSearch(student):
    
    # Store best match and highest weight of a room below: 
    bestMatch = potentialRooms[0]
    highestWeight = 0
    
    # For each of the potential rooms, get a weight
    for i in range(len(potentialRooms)):
        w = weightRoom(potentialRooms[i], student)
        
        # If current weight is greater than highest weight, update bestMatch and highest weight
        if (w > highestWeight):
            bestMatch = potentialRooms[i]
            highestWeight = i
    
    # Checking sex of best match
    # e = empty? 
    if (bestMatch["sex"] == "e"):
        bestMatch["sex"] = student["sex"]

    # Add the student to the "occupants in the room"
    bestMatch["occupants"].append(student)
    # Update student dorm name to the best match 
    student["dorm"] = bestMatch["name"]

    return bestMatch # End function 

# -----------------------------------------------------------------------------------------------------------------

# Start of firstSearch 

# Function: isPerfectMatch 
# Description: Looks to see if two students have commonality
# Parameters: Takes a Room and a Student [2 dictionaries]
# Returns: True if student can fit well into the room, False otherwise
def isPerfectMatch(room, student):

    commonalityScore = 0    # Determine if student is valid for 

    # Loop through all students in a room and check too see if student would fit in here 
    for occupant in room["occupants"]:

        # Major takes priority if determinging commonality between two students 
        commonalityScore += 5 if (occupant["major"] == student["major"]) else 0

        # Check to see if students are from the same place    
        commonalityScore += 1 if (occupant["geo"] == student["geo"]) else 0

        # Following checks sleep hours making sure the two students sleep within a good time with one another
        for sleepIndex in range(2):
            if (occupant["sleepHours"][sleepIndex] == student["sleepHours"][sleepIndex] or 
                occupant["sleepHours"][sleepIndex] + 1 == student["sleepHours"] or 
                occupant["sleepHours"][sleepIndex] - 1 == student["sleepHours"]         ):
                commonalityScore += 1
        
        # Following checks music preferences
        for music in occupant["musicPreference"]:
            commonalityScore += 1 if (music in student["musicPreference"]) else 0
        
        # Following checks hobbies 
        for k in occupant["hobbies"]:
            commonalityScore += 1 if (music in student["hobbies"]) else 0

    # CommonalityScore threshold is 4 [SUBJECT TO CHANGE]
    if (commonalityScore > 4): 
        return True
    return False

# Function: firstSearch
# Description: if there is a "perfect" fit, it matches the student there, otherwise collecting other
# decent fits to use in a sort of ideal search
# Parameters: data/campus information and student information [Two dictionaries]
# Returns: True on sucess, False otherwise  
def firstSearch(data, student):

    # Make sure that the global list of potential rooms is empty
    potentialRooms.clear()

    if (len(student["dormPref"]) != 0): # if there is a preferred dorm, look through those
        
        # move through dorm prefs - later on we can just move the iterablle to specific points in the array
        for preference in student["dormPref"]:
            
            dormList = data.keys()  # list of dorms to use as keys

            for dorm in dormList:
                if (preference in dorm): # find preferred dorm
                    
                    # see if possible to move into room
                    if ((student["sex"] == data[dorm]["sex"] or data[dorm]["sex"] == "e" or data[dorm]["sex"] == "i") and 
                        student["year"] == data[dorm]["year"] and 
                        len( data[dorm]["occupants"] ) < data[dorm]["size"]) and data[dorm]["ra room"] == False:

                        # If there are occupants let's see if the student is a good match 
                        if (len(data[dorm]["occupants"]) > 0):
                            # Calling is Perfect Match, 
                            if (isPerfectMatch(data[dorm], student)):
                                # Add student to the dorm room as a occupant 
                                data[dorm]["occupants"].append(student)
                                # Return True on success
                                return True
                            # Add to potential rooms
                            else:
                                potentialRooms.append(data[dorm])

                        # IF dorm room is empty just add it 
                        if (len(data[dorm]["occupants"]) == 0):
                            potentialRooms.append(data[dorm])

    # Case where no potential rooms are found 
    if (len(potentialRooms) == 0):
        
        # Again get a list of dorm keys 
        dormList = data.keys()

        for dorm in dormList:
            
            # Same checks from code above
            if ((student["sex"] == data[dorm]["sex"] or data[dorm]["sex"] == "e" or data[dorm]["sex"] == "i") and student["year"] == data[dorm]["year"] and 
                len(data[dorm]["occupants"]) < data[dorm]["size"] and data[dorm]["ra room"] == False):
                
                # for k in data[j]["occupants"]:
                #     if k["name"] == student["name"]:
                #         return False

                if (len(data[dorm]["occupants"]) > 0):
                    if (isPerfectMatch(data[dorm], student)):
                        data[dorm]["occupants"].append(student)
                        return True
                    else:
                        potentialRooms.append(data[dorm])

                if (len(data[dorm]["occupants"]) == 0):
                    potentialRooms.append(data[dorm])
    
    # if no potential rooms we can perform an ideal search for the student
    if (len(potentialRooms) != 0):
        idealSearch(student)
        return True
    # Return false if first search has failed 
    else:
        return False

# Empty Function, unfinished by Jack, Probably useless 
def groupSort(students):

    return