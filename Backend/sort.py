# what I maybe plan to do is that if there are no "perfect" matches,
# collect rooms that are good matches and sort between those and pick
# the best of them - this sort of emulates a best fit and ideal fit at
# the same time (will be two seperate sort functions *if a perfect fit
# is not found*)

# i want to have it working with just induvial students before I implement
# groups 

potentialRooms = []

def idealSearch(student):



    return

# looks to see if two students have commonality
def isPerfectMatch(room, student):

    i = 0

    for i in room["occupants"]:
        if (i["major"] == student["major"]):
            i += 3

        if (i["geo"] == student["geo"]):
            i += 1

    if (i > 3):
        return True

    return False

# if there is a "perfect" fit, it matches the student there, otherwise collecting other
# decent fits to use in a sort of ideal search
def firstSearch(data, student):

    potentialRooms.clear()

    if (len(student["dormPref"]) != 0): # if there is a preferred dorm, look through those
        
        while (student["dorm"] == ""): 
            
            # move through dorm prefs  - later on we can just move the iterablle to specific points in the array
            i = 0        
            dorm = data.keys()  # list of dorms to use as keys

            for j in dorm:
                if (student["dormPref"][i] in j):   # find preferred dorm
                    
                    # see if possible to move into room
                    if (student["sex"] == data[j]["sex"] or data[j]["sex"] == "e" and student["year"] == data[j]["year"]):
                        if (len(data[j]["occupants"]) > 0):
                            if (isPerfectMatch(data[j], student)):
                                data[j]["occupants"].append(student)

                                return True
                            else:
                                potentialRooms.append(data[j])

                        if (len(data[j]["occupants"]) == 0):
                            potentialRooms.append(data[j])

            i += 1

    if (len(potentialRooms) == 0):
        dorm = data.keys()

        for j in dorm:
            if (student["sex"] == data[j]["sex"] or data[j]["sex"] == "e" and student["year"] == data[j]["year"]):
                if (len(data[j]["occupants"]) > 0):
                    if (isPerfectMatch(data[j], student)):
                        data[j]["occupants"].append(student)

                        return True
                    else:
                        potentialRooms.append(data[j])

                if (len(data[j]["occupants"]) == 0):
                    potentialRooms.append(data[j])
               
    idealSearch(student)