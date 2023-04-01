# Implement Algorithm Here:
import json
# -ideal_search: Finds a room with a size that matches the group size and takes preferences into account

def idealSearch(name, data, groupSize, preferred):
    # check to see if groupSize matches the room size available
    # preferred is a list of their preferred dorms in order from first to last, can be up to 3 <= x <= 5 dorms
    # returns a string of the best dorm available for them
    # data is read from a json file
    # if group size is alr 4, just get them a room
    if groupSize == 2:
        # if groupsize is 2 for a double (basically fresh housing or quad)
        first_choice = preferred[0]
        hall = data[first_choice]
        count = 0
        for i in hall:
            room_one = hall[i]
            occ = room_one["Occupants"]
            size_ = room_one["size"]
            if len(occ) == 0:
                occ.append(name)
                count += 1
        if count == 0:
            next_choice = preferred[1]
            hall = data[next_choice]
            for i in hall:
                room_one = hall[i]
                occ = room_one["Occupants"]
                size_ = room_one["size"]
                if len(occ) < size_:
                    occ.append(name)
                    count+=1
                    break
    # check each preferred building in order
    first_choice = preferred[0]
    hall = data[first_choice]
    for i in hall:
        room_one = hall[i]
        occ = room_one["Occupants"]
        size_ = room_one["size"]
        if len(occ) < size_:
            occ.append(name)
            break

    return data

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
groupSize = 4
preferred1 = ["Warren", "Nason", "Davison"]
preferred2 = ["Sharp", "Hall"]
name = ["kellie", "nancy"]
data = idealSearch(name, data, groupSize, preferred1)
printData(data)