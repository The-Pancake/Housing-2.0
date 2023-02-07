def sortFucntion(data, student):

    if (len(student["dormPref"]) != 0):
        
        while (student["dorm"] == ""): 

            i = 0               # move through dorm prefs
            dorm = data.keys()  # list of dorms

            for j in dorm:
                if (student["dormPref"][i] in j):   # find preferred dorm
                    
                    # see if possible to move into room
                    if (student["sex"] == data[j]["sex"] and student["year"] == data[j]["year"]):
                        if (len(data[j]["occupants"]) == 0):
                            data[j]["occupants"].append(student["name"])


                    return True
               
    return False