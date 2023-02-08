# what I maybe plan to do is that if there are no "perfect" matches,
# collect rooms that are good matches and sort between those and pick
# the best of them
potentialRooms = []

# looks to see if two students have commonality
def isMatch(room, student):

    return True

# what does the actual sort
def sortFucntion(data, student):

    if (len(student["dormPref"]) != 0):
        
        while (student["dorm"] == ""): 

            i = 0               # move through dorm prefs
            dorm = data.keys()  # list of dorms

            for j in dorm:
                if (student["dormPref"][i] in j):   # find preferred dorm
                    
                    # see if possible to move into room
                    if (student["sex"] == data[j]["sex"] or data[j]["sex"] == "e" and student["year"] == data[j]["year"]):
                        if (len(data[j]["occupants"]) == 0):
                            data[j]["occupants"].append(student["name"])
                            data[j]["sex"] = student["sex"]

                            return True
                        if (len(data[j]["occupants"]) == 1):
                            isMatch(data[j], student)


                    i += 1
                        


                    
               
    return False