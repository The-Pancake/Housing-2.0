import json
import copy

'''
Will try to search for rooms with connected bathrooms in preferred dorms of the group preference
'''
def General_Split_Search(group_list,campus):
  group_size = len(group_list)
  buildings = campus.keys()
  print(buildings)

  middle_index = group_size // 2

  group1 = group_list[:middle_index]
  group2 = group_list[middle_index:]

  for dorm in campus:#loops through all the dorms in the groups preferred list
    for room in campus[dorm]:#loops through the rooms in the building
      #if the room size does not fit the group or it is occupied
      if campus[dorm][room]["size"] != len(group1) or len(campus[dorm][room]["Occupants"]) > 0: 
        continue
      else:
        if campus[dorm][room]["shared_bathroom"] != False:
          connected_room = str(campus[dorm][room]["shared_bathroom"])
          if campus[dorm][connected_room]["size"] == len(group2) and len(campus[dorm][connected_room]["Occupants"]) == 0:
            campus[dorm][room]["Occupants"] = copy.deepcopy(group1)
            campus[dorm][connected_room]["Occupants"] = copy.deepcopy(group2)
            # a = open('C:/Users/dongm2/Documents/RPI/Personal_projects/Rcos/objects_changed.json', 'w')
            # json.dump(campus,a, indent = 2)
            # a.close()
            return True
  return False

if __name__ == '__main__':
  campus = open("./Campus_data_structures/campus3.json")
  campus = json.load(campus)
  group = ["Dom", "Bob", "Paul", "Ben"]
  dorm_pref = ["Hall"]
  if General_Split_Search(group,campus):
    print(campus)
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
