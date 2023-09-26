import json

def idealSearch(data, groupSize, preferred, students):
    for pref in preferred:
        hall = data.get(pref, {})
        for room_id, room_data in hall.items():
            occupants = room_data["Occupants"]
            size = room_data["size"]
            if len(occupants) + groupSize <= size:  # Check if groupSize can fit in the room
                for student in students:
                    occupants.append(student)
                room_data["Occupants"] = occupants
                return True, pref + " " + room_id
            elif len(occupants) == 0 and groupSize <= size:  # If room is empty, assign if groupSize can fit
                for student in students[:size]:
                    occupants.append(student)
                room_data["Occupants"] = occupants
                return True, pref + " " + room_id
    return False, None

def updateJSON(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def printData(data):
    for hall, rooms in data.items():
        print(hall, ":")
        for room_id, room_data in rooms.items():
            print("  ", room_id, ":")
            print("    room number:", room_data["id"])
            print("    room size:", room_data["size"])
            print("    shared bathroom:", room_data["shared_bathroom"])
            print("    type:", room_data["type"])
            print("    occupants:")
            for occupant in room_data["Occupants"]:
                print("\t", occupant)

