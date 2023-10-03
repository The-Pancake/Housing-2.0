import json

def findAvailableRoom(data, groupSize, students):
    for hall, rooms in data.items():
        for room_id, room_data in rooms.items():
            occupants = room_data["Occupants"]
            size = room_data["size"]
            if len(occupants) + groupSize <= size:
                for student in students:
                    occupants.append(student)
                room_data["Occupants"] = occupants
                return True, hall + " " + room_id
    return False, None

def updateJSON(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def printData(data):
    for hall, rooms in data.items():
        print(hall, ":")
        for room_id, room_data in rooms.items():
            print("  ", room_id, ":")
            print("    room size:", room_data["size"])
            print("    shared bathroom:", room_data["shared_bathroom"])
            print("    type:", room_data["type"])
            print("    occupants:")
            for occupant in room_data["Occupants"]:
                print("\t", occupant)

# Load the JSON data
filename = "Backend/Campus_data_structures/campus3.json"
with open(filename) as f:
    data = json.load(f)

students = ["John", "Bill"]
groupSize = len(students)

room_found, given_room = findAvailableRoom(data, groupSize, students)

if room_found:
    updateJSON(filename, data)
    print("Room found:", given_room)
else:
    print("No suitable room found for the group.")
    
printData(data)
