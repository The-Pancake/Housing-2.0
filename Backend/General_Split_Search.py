from pymongo import MongoClient
import copy

'''
Will try to search for rooms with connected bathrooms in preferred dorms of the group preference
'''
def connect_to_db(uri):
    client = MongoClient(uri)
    db = client['Campus'] 
    return db

def General_Split_Search(group_list, db):
    group_size = len(group_list)
    middle_index = group_size // 2
    group1 = group_list[:middle_index]
    group2 = group_list[middle_index:]

    dorms = db.rooms.find()
    for dorm in dorms:
        dorm_name = dorm["dorm_name"]
        room_id = str(dorm["_id"])
        occupants = dorm.get("Occupants", [])

        if dorm["size"] != len(group1) or len(occupants) > 0:
            continue
        else:
            if dorm["shared_bathroom"] != False:
                connected_room = db.rooms.find_one({"_id": dorm["shared_bathroom"]})
                if not connected_room:
                    continue

                if connected_room["size"] == len(group2) and len(connected_room["Occupants"]) == 0:
                    db.rooms.update_one({"_id": dorm["_id"]}, {"$set": {"Occupants": copy.deepcopy(group1)}})
                    db.rooms.update_one({"_id": connected_room["_id"]}, {"$set": {"Occupants": copy.deepcopy(group2)}})
                    return True
    return False

# Connection URI
uri = "mongodb+srv://housing20rcos:nQWnpyw4PsFk78eJ@housing2.elxx6hn.mongodb.net/?retryWrites=true&w=majority"

# Connect to MongoDB
try:
    db = connect_to_db(uri)
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    exit()
    
if __name__ == '__main__':
  dorm_pref = ["Hall"]
  group = ["Dom", "Bob", "Paul", "Ben"]
  if General_Split_Search(group, db):
      # Fetch the updated rooms and print them.
      rooms = db.rooms.find()
      for room in rooms:
          print(room)
  else:
        print("did not find room for group :(")
  # Things to test for:
  #   - if all rooms are empty
  #   - if all rooms are Full
  #   - if some rooms are Full
  #   - if no rooms have a shared bathroom? (may created a list of dorms that have shared bathroom)
  #   note: hierarchy
            # -search for full group (preferences)
            # -search split for group (to potentially find housing in their preferences)
            # -search for full group (no preferences)

            # full group
            # split group
            # near group
            # near building group
