# what I maybe plan to do is that if there are no "perfect" matches,
# collect rooms that are good matches and sort between those and pick
# the best of them - this sort of emulates a best fit and ideal fit at
# the same time (will be two seperate sort functions *if a perfect fit
# is not found*)

# i want to have it working with just induvial students before I implement
# groups - though that shouldn't be hard since groups will pretty much always
# fit under the perfect fit category of things

# September 19th, 2023 Changes - Daniel He 
# - Going to review/ modify code written by Jack adding comments 

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

# Weighs a room based  on a bunch of variables - to change, currently acts as just an example 
# of what it will be, function is very flexible and can always add more comparisons
# Helper for ideal search 
def weightRoom(room, currStudent):

    # Holds room weight 
    weight = 0

    # Searches through occupants calculating weight based on a variety of factors
    # aStudent represents a occupant in the room 
    for aStudent in room["occupants"]:
        # Compare majors
        weight += 5 if (aStudent["major"] == currStudent["major"]) else weight

        # Compare geography (aka where they are from )
        weight += 3 if (aStudent["geo"] == currStudent["geo"]) else weight
        
        # Compare sleep hours, this is stored as a array where the sleep hours of a student looks like this:
        #
        # [ (Start Bedtime), (End Bedtime) ]
        #         0              1           
        #
        for sleepIndex in range(2):
            if( sleepIndex < 2 ): 
                weight += 1 if aStudent["sleepHours"][sleepIndex] == currStudent["sleepHours"][sleepIndex] else weight 

        # Compare music preference between the two students
        for musicPref in aStudent["musicPreference"]:
            weight += 1 if (musicPref in currStudent["musicPreference"]) else weight
        
        # Compare hobbies between the two students
        for hobby in aStudent["hobbies"]:
            weight += 1 if (hobby in currStudent["hobbies"]) else weight

    # If there is no one in the room we increase the weight
    if (weight == 0 and len(room["occupants"]) == 0):
        weight += 1

    # Increase the weight if the room is in a dorm of a student's preference
    # 
    weight += 5 if (room["name"] in currStudent["dormPref"]) else weight

    # Jacks original code for calculating weight if dorm room is a student's preference
    # k = 0
    # for dorm in currStudent["dormPref"]:
    #     if (dorm == room["name"]):
    #         weight += 5 - k
    #         k += 1

    # Return calculated weight
    return weight


# After first search, uses potentialRooms to look
def idealSearch(student):
    
    # Store best match and highest weight of a room below: 
    bestMatch = potentialRooms[0]
    highestWeight = 0

    # For each of the potential rooms, get a weight
    for i in range(len(potentialRooms)):
        w = weightRoom(potentialRooms[i], student)
        
        # If current weight is greater than highst weight, update bestMatch and highest weight
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

    return # End function 

# -----------------------------------------------------------------------------------------------------------------
# Start of firstSearch 
# looks to see if two students have commonality
def isPerfectMatch(room, student):

    i = 0

    for j in room["occupants"]:
        if (j["major"] == student["major"]):
            # print("same major")
            i += 5

        if (j["geo"] == student["geo"]):
            i += 1

        for k in range(2):
            if (j["sleepHours"][k] == student["sleepHours"][k] or j["sleepHours"][k] + 1 == student["sleepHours"] or j["sleepHours"][k] - 1 == student["sleepHours"]):
                i += 1
        
        for k in j["musicPreference"]:
            if (k in student["musicPreference"]):
                i += 1
        
        for k in j["hobbies"]:
            if (k in student["musicPreference"]):
                i += 1
        

    if (i > 4): 
        return True

    return False

# if there is a "perfect" fit, it matches the student there, otherwise collecting other
# decent fits to use in a sort of ideal search
def firstSearch(data, student):

    potentialRooms.clear()

    if (len(student["dormPref"]) != 0): # if there is a preferred dorm, look through those
        
        for i in student["dormPref"]:
            
            # move through dorm prefs - later on we can just move the iterablle to specific points in the array
            dorm = data.keys()  # list of dorms to use as keys

            for j in dorm:
                if (i in j): # find preferred dorm
                    
                    # see if possible to move into room
                    if ((student["sex"] == data[j]["sex"] or data[j]["sex"] == "e" or data[j]["sex"] == "i") and student["year"] == data[j]["year"] and 
                    len(data[j]["occupants"]) < data[j]["size"]) and data[j]["ra room"] == False:
                        
                        # for k in data[j]["occupants"]:
                        #     if k["name"] == student["name"]:
                        #             return False
                    
                        if (len(data[j]["occupants"]) > 0):
                            
                            if (isPerfectMatch(data[j], student)):
                                data[j]["occupants"].append(student)

                                return True
                            else:
                                potentialRooms.append(data[j])

                        if (len(data[j]["occupants"]) == 0):
                            potentialRooms.append(data[j])

    # the case in no dorm pref, or if it couldn't find it regardless
    if (len(potentialRooms) == 0):
        dorm = data.keys()
        # print(student)
        for j in dorm:

            if ((student["sex"] == data[j]["sex"] or data[j]["sex"] == "e" or data[j]["sex"] == "i") and student["year"] == data[j]["year"] and 
                len(data[j]["occupants"]) < data[j]["size"] and data[j]["ra room"] == False):
                #print(student)
                
                # for k in data[j]["occupants"]:
                #     if k["name"] == student["name"]:
                #         return False
                
                if (len(data[j]["occupants"]) > 0):
                    
                    if (isPerfectMatch(data[j], student)):
                        
                        data[j]["occupants"].append(student)

                        return True
                    else:
                        potentialRooms.append(data[j])

                if (len(data[j]["occupants"]) == 0):
                    potentialRooms.append(data[j])
               
    if (len(potentialRooms) != 0):
        idealSearch(student)
    else:
        return False
    

# Empty Function, unfinished 
def groupSort(students):

    return