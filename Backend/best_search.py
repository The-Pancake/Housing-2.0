# Implement Algorithm Here:
import json
from operator import truediv
#import sort
def check_Year(student1,student2):
    if (student1["year"] == student2["year"]):
        return True
    return False


#this is so unbelievabley inefficent, i'm figuring out a way to make it better
def check_groupSize(group, campus, building, floor, room):
    for building in campus:
        for floor in campus[building]:
            for room in data[building][floor]:
                room_size = data[building][floor][room]['size']
    if (room_size == len(group["group"])):
        return True, len(group["size"])
    return False

#i'm reworking this since i rewrote the other two functions
def bestSearch(group,room):
    gs = list(check_groupSize(group,room))
    occupants = room["Occupants"]
    if (gs[0] == True):
        for i in room["size"]:
            if(i["size"] == gs[1]):
                for j in group['group']:
                    occupants.append(gs[0])

class Rooms:
    def __init__(room, building, gender, num, size, bathroom, year, occupants):
        room.building = building
        room.gender = gender
        room.num = num
        room.size = size
        room.bathroom = bathroom
        room.year = year
        room.occupants = occupants

def bestSearch():
    return


if __name__ == "__main__":
    
    #reading data from JSON file
    with open("test.json") as json_file:
        data = json.load(json_file)
        
        
    #creating an array of objects with all the data in test file
    allrooms = []
    
    for room in data:
        currRoom = data[room]
        name = currRoom['name']
        gender = currRoom['sex']
        num = currRoom['id']
        bathroom = False;
        size = currRoom['size']
        year = currRoom['year']
        occupants = currRoom['occupants']
        newRoom = Rooms(name, gender, num, size, bathroom, year, occupants)
        allrooms.append(newRoom)

