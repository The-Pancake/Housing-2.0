# Implement Algorithm Here:
import json
# -ideal_search: Finds a room with a size that matches the group size and takes preferences into account

def idealSearch(name, data, groupSize, preferred):
    # check to see if groupSize matches the room size available
    # preferred is a list of their preferred dorms in order from first to last, can be up to 3 <= x <= 5 dorms
    # returns a string of the best dorm available for them
    # data is read from a json file
    # if group size is alr 4, just get them a room
    given_dorm = ""
    room = ""
    if groupSize == 2 or groupSize == 4:
        # if groupsize is 2 for a double (basically fresh housing or quad)
        # what it needs to do: add one person to a room w one person
        first_choice = preferred[0]
        hall = data[first_choice]
        count = 0
        for i in hall:
            room_one = hall[i]
            occ = room_one["Occupants"]
            size_ = room_one["size"]
            if len(occ) == 0:
                for x in name:
                    occ.append(x)
                count += 1
                room = first_choice
                break
        if count == 0:
            next_choice = preferred[1]
            room = next_choice
            hall = data[next_choice]
            for i in hall:
                room_one = hall[i]
                occ = room_one["Occupants"]
                size_ = room_one["size"]
                if len(occ) < size_:
                    for x in name:
                        occ.append(x)
                    count+=1
                    break
    elif groupSize == 1:
        first_choice = preferred[0]
        hall = data[first_choice]
        count = 0
        for i in hall:
            room_one = hall[i]
            occ = room_one["Occupants"]
            size_ = room_one["size"]
            if len(occ) == 1:
                for x in name:
                    occ.append(x)
                count += 1
                room = first_choice
                break
    
    given_dorm = room + " " + room_one["id"]

    return data, given_dorm

def printData(data):
    for i in data:
        print(i, ":")
        data_set = data[i]
        for j in data_set:
            print("  ", j, ":")
            data_s = data_set[j]
            id_ = data_s["id"]
            size = data_s["size"]
            shared_bath = data_s["shared_bathroom"]
            type_ = data_s["type"]
            occupants = data_s["Occupants"]
            print("    room number:", id_, "\n    room size:", size)
            print("    shared bathroom:", shared_bath, "\n    type:", type_)
            print("    occupants:")
            for x in occupants:
                print("\t", x)

f = open("test.json")
data = json.load(f)
preferred1 = ["Warren", "Nason", "Davison"]
preferred2 = ["Sharp", "Hall"]
name = ["kellie"]
groupSize = len(name)
data, given_room = idealSearch(name, data, groupSize, preferred1)
printData(data)
print(given_room)
