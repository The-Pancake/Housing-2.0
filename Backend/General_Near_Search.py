import copy

#General Near Search algorithm:
# Argurments:
#   grouplist: a list of the name of students in a group
#   campus: dictionary that has data of the campus dorms and info contain within them (json file converted in "main")
#In the case that General search and Ideal search fail to find a room for a group
#this algorithm splits the groups up and tries to find 2 rooms within the same building to assign
#the students to
def General_Near_Search(group_list,campus):
  group_size = len(group_list)
  buildings = campus.keys()
  # print(buildings) #used for checking if the buildings are read in correctly

  middle_index = group_size // 2

  #divide the group up into two and default rooms found to false
  group1 = group_list[:middle_index]
  group2 = group_list[middle_index:]
  room1_found = False
  room2_found = False
  for dorm in buildings:#loops through all the dorms
    room_id1 = -1 #variables to store room id's
    room_id2 = -1
    #loops through the rooms in the building and checks:
    # if the current room is empty and if so store the room id and trigger room found flag to true
    for room in campus[dorm]:#loops through the rooms in the building
      if len(campus[dorm][room]["Occupants"]) == 0:
        room_id1 = room
        room1_found = True
        
        for room in campus[dorm]:
          if len(campus[dorm][room]["Occupants"]) == 0 and room != room_id1:
            room_id2 = room
            room2_found = True

    #if two rooms can be found within the same building, assign the rooms to the group
    if room1_found and room2_found:
      campus[dorm][room_id1]["Occupants"] = copy.deepcopy(group1)
      campus[dorm][room_id2]["Occupants"] = copy.deepcopy(group2)
      return True
  return False
