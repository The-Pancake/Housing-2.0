import copy
import json
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
def Ideal_Near_Search(group_list,group_preferences,campus):
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
      if len(campus[dorm][room1]["Occupants"]) == 0:
        room_id1 = room1
        room1_found = True
        
        for room2 in campus[dorm]:
          if len(campus[dorm][room2]["Occupants"]) == 0 and room2 != room_id1:
            room_id2 = room2
            room2_found = True

    #if two rooms can be found within the same building, assign the rooms to the group
    if room1_found and room2_found:
      campus[dorm][room_id1]["Occupants"] = copy.deepcopy(group1)
      campus[dorm][room_id2]["Occupants"] = copy.deepcopy(group2)
      return True
  return False

if __name__ == '__main__':
  campus = open("./Campus_data_structures/campus3.json")
  campus = json.load(campus)
  group = ["Dom", "Bob", "Paul", "Ben"]
  dorm_pref = ["warren"]
  if Ideal_Near_Search(group,dorm_pref,campus):
    print(campus)
  else:
    print("did not find room for group :(")
  # for x in campus:
  #   for y in campus[x]:
  #     str = "string " + y + " has int:"
  #     print(str,int(y))