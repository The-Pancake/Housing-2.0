import copy
#do we priortize earlier four person group (now two 2person groups), or later 2 person group?
#fiure out all different ways rpi labels rooms (letters,numbers,letters and numbers?)

#Ideal Near Search algorithm:
# Argurments:
#   grouplist: a list of the name of students in a group
#   group_preferences: a list of of dorm names that the group would like to stay in
#   campus: dictionary that has data of the campus dorms and info contain within them (json file converted in "main")
#In the case that General search and Ideal search fail to find a room for a group
#this algorithm splits the groups up and tries to find 2 rooms within the same building (building is selected from their list) to assign
#the students to
def ideal_near_seach(group_list,group_preferences,campus):
  group_size = len(group_list)
  # print(buildings) #used for checking if the buildings are read in correctly

  middle_index = group_size // 2

  #divide the group up into two and default rooms found to false
  group1 = group_list[:middle_index]
  group2 = group_list[middle_index:]
  room1_found = False
  room2_found = False
  for dorm in group_preferences:#loops through all the dorms in the groups' preferred list
    room_id1 = -1 #variables to store room id's
    room_id2 = -1
    #loops through the rooms in the building and checks:
    # if the current room is empty and if so store the room id and trigger room found flag to true
    for room1 in campus[dorm]:#loops through the rooms in the building
      if len(room1["Occupants"]) == 0:
        room_id1 = room1["id"]
        room1_found = True

    for room2 in campus[dorm]:
      if len(room1["Occupants"]) == 0 and room2["id"] != room_id1:
        room_id2 = room2["id"]
        room2_found = True
        
    #if two rooms can be found within the same building, assign the rooms to the group
    #note: may change campus data structure to remove for-loop here
    if room1_found == True and room2_found == True:
      for room in campus[dorm]:
        if room["id"] == room_id1:
          room["Occupants"] = copy.deepcopy(group1)
        if room["id"] == room_id2:
          room["Occupants"] = copy.deepcopy(group2)
      return True
  return False
