import copy

def best_near_seach(group_list,campus):
  group_size = len(group_list)
  buildings = campus.keys()
  # print(buildings) #used for checking if the buildings are read in correctly

  middle_index = group_size // 2

  group1 = group_list[:middle_index]
  group2 = group_list[middle_index:]
  room1_found = False
  room2_found = False
  for dorm in buildings:#loops through all the dorms in the groups preferred list
    room_id1 = -1
    room_id2 = -1
    for room1 in campus[dorm]:#loops through the rooms in the building
      if len(room1["Occupants"]) == 0:
        room_id1 = room1["id"]
        room1_found = True

    for room2 in campus[dorm]:
      if len(room1["Occupants"]) == 0 and room2["id"] != room_id1:
        room_id2 = room2["id"]
        room2_found = True
    
    if room1_found == True and room2_found == True:
      for room in campus[dorm]:
        if room["id"] == room_id1:
          room["Occupants"] = copy.deepcopy(group1)
        if room["id"] == room_id2:
          room["Occupants"] = copy.deepcopy(group2)
      return True
  return False