# Implement Algorithm Here:

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
