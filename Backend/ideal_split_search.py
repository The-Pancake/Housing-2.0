from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

'''
Will try to search for rooms with connected bathrooms in preferred dorms of the group preference

NOTE: In this case "campus" is the dictionary we will modify to put a student into a room
'''
def Ideal_Split_Search(group_list, dorms, campus_dorm_rooms):
  group_size = len(group_list)
  middle_index = group_size // 2
  group1 = group_list[:middle_index]
  group2 = group_list[middle_index:]

  if len(group1) == len(group2):
    for dorm in dorms:
      query = {
        "Dorm": dorm,
        "Size": len(group1),
        "ShareBathroom": True,
        "Occupants" : {"$size" : 0}
      }
      rooms = list(campus_dorm_rooms.find(query))
      for room1 in rooms:
        query1 = {
          "Dorm": room1.get("Dorm"),
          "Size": len(group2),
          "shareBathroom": True,
          "shareRoom": room1.get("RoomNum"),
          "Occupants" : {"$size" : 0}
        }
        room2 = list(campus_dorm_rooms.find(query1))
        if len(room2) == 0:
          room1_id = room1.get("_id")
          room2_id = room2[0].get("_id")
          campus_dorm_rooms.update_one({"_id":room1_id}, { "$set" : {"Occupants": group1}})
          campus_dorm_rooms.update_one({"_id":room2_id}, { "$set" : {"Occupants": group2}})
          return True
  else:
    for dorm in dorms:
      query = {
        "Dorm": dorm,
        "Size": len(group1),
        "ShareBathroom": True,
        "Occupants" : {"$size" : {"$lte": {"$expr": {"$subtraction": ["Size", len(group1)]} } } }
      }
      rooms = list(campus_dorm_rooms.find(query))
      for room1 in rooms:
        query1 = {
          "Dorm": room1.get("Dorm"),
          "Size": len(group2),
          "shareBathroom": True,
          "shareRoom": room1.get("RoomNum"),
          "Occupants" : {"$size" : 0}
        }
        room2 = list(campus_dorm_rooms.find(query1))
        if len(room2) > 0:
          room1_id = room1.get("_id")
          room2_id = room2[0].get("_id")

          room1_occupants = room1[0].get("Occupants")
          new_group1 = room1_occupants + group1

          campus_dorm_rooms.update_one({"_id":room1_id}, { "$set" : {"Occupants": new_group1}})
          campus_dorm_rooms.update_one({"_id":room2_id}, { "$set" : {"Occupants": group2}})
          return True
  return False



if __name__ == '__main__':
  uri = "mongodb+srv://housing20rcos:nQWnpyw4PsFk78eJ@housing2.elxx6hn.mongodb.net/?retryWrites=true&w=majority"
  dorms = ["Blitman", "Warren", "Hall"]
  group = ["Tom", "Bob", "Tim", "Bib"]

  client = MongoClient(uri, server_api=ServerApi('1'))
  campus = client["Campus"]
  campus_dorm_rooms = campus["Dorms_Michael"]
  Ideal_Split_Search(group, dorms, campus_dorm_rooms)