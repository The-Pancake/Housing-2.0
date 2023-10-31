import copy
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

#General Near Search algorithm:
# Argurments:
#   grouplist: a list of the name of students in a group
#   campus: dictionary that has data of the campus dorms and info contain within them (json file converted in "main")
#In the case that General search and Ideal search fail to find a room for a group
#this algorithm splits the groups up and tries to find 2 rooms within the same building to assign
#the students to
def General_Near_Search(group_list, dorms, campus_dorm_rooms):
  group_size = len(group_list)
  

  middle_index = group_size // 2
  group1 = group_list[:middle_index]
  group2 = group_list[middle_index:]

  for dorm in dorms:
    query = {
        "$and" : [
          {"Dorm": dorm},
          {"Size": 2},
          {"Occupants" : {"$size" : 0}}
        ]
    }
    rooms = list(campus_dorm_rooms.find(query))
    
    if len(rooms) < 2:
      continue
    else:
      room1_id = rooms[0].get("_id")
      room2_id = rooms[1].get("_id")
      campus_dorm_rooms.update_one({"_id":room1_id}, { "$set" : {"Occupants": group1}})
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
  General_Near_Search(group, dorms, campus_dorm_rooms)



