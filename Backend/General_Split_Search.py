
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


'''
Will try to search for rooms with connected bathrooms in preferred dorms of the group preference
'''

def Ideal_Split_Search(group_list,campus_dorm_rooms):
  group_size = len(group_list)
  middle_index = group_size // 2
  group1 = group_list[:middle_index]
  group2 = group_list[middle_index:]
  query1 = {
    "Size": len(group1),
    "ShareBathroom": True,
    "Occupants" : {"$size" : 0}
  }
  
  rooms = list(campus_dorm_rooms.find(query1))
  for room1 in rooms:
    query2 = {
      "Dorm": room1.get("Dorm"),
      "Size": len(group2),
      "shareBathroom": True,
      "shareRoom": room1.get("RoomNum"),
      "Occupants" : {"$size" : 0}
    }
    room2 = list(campus_dorm_rooms.find(query2))
    if len(room2) :
      room1_id = room1.get("_id")
      room2_id = room2[0].get("_id")
      campus_dorm_rooms.update_one({"_id":room1_id}, { "$set" : {"Occupants": group1}})
      campus_dorm_rooms.update_one({"_id":room2_id}, { "$set" : {"Occupants": group2}})
      return True
  return False


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
