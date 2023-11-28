from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

import General_Near_Search as GNS
import Ideal_near_search as INS
import General_Split_Search as GSS
import ideal_split_search as ISS
#import Best_Near_Building_Search as BNBS

if __name__ == '__main__':
  uri = "mongodb+srv://housing20rcos:nQWnpyw4PsFk78eJ@housing2.elxx6hn.mongodb.net/?retryWrites=true&w=majority"
  client = MongoClient(uri, server_api=ServerApi('1'))

  group = client["Student_Info"]
  groups = group["Groups_Michael"]

  all_groups = list(groups.find())

  sorted_groups = sorted(all_groups, key=lambda x: (-len(x.get("members")), x.get("Date")))
  print(sorted_groups)
  """
    groupList = []
    singlesList = []
    for i in sorted_groups:
      if len(sorted_groups[i].get(members)) > 1:
        groupsList.append(sorted_groups[i])
      else:
        singlesList.append(sorted_groups[i])



    Remaining_groups = []
    for GROUP in groupList:
      GPref = GROUP.get("Preferences")
      GMembers = GROUP.get("members")

      if not Ideal_search:
        if not GeneralSearch:
          if not Ideal_split_Search:
            if not General_split_search:
              if not Ideal_near_search:
                if not General_near_search:
                  if not near_building_search:
                    Remaining_groups.append(GMembers) or something
    for person in singlesList:
      if not singlesThing:
        do something with left over person?
    
  """
    