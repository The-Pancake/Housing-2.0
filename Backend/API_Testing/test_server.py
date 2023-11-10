import requests
import sys
import json 
import uvicorn

sys.path.append('/home/beef-patty/Desktop/Housing2.0_Fall_2023/Housing-2.0/Backend')
sys.path.append('/home/beef-patty/Desktop/Housing2.0_Fall_2023/Housing-2.0/Backend/Database/dorm_data')

import sortSingles
import mongodb_test as mb
import json_comparator as jc

if __name__ == "__main__": 
    

    # Grab a student from the front end
    john = requests.get("http://127.0.0.1:8000/students/0/").json()

    
    # Grab dorm information from backend 
    database = mb.connect_to_database("Campus")
    collection = database["Dorms_Daniel"]
    data = mb.get_all_data(collection)
    
    # Formatted Data [TEMPORARY, reason explained below]
    formattedData = {}

    # Testing it by printing it all out.
    i = 0
    print('===================================================')
    for item in data: 
        id, room = item
        print( json.dumps(room, indent=4))
        # Print room info to make sure everything is correct
        # print( json.dumps(item.get(room), indent=4 ) )
        print('===================================================')

        formattedData[room] = item.get(room)    


    # Next we can finally call sortSingles and see where john will be placed 
    print(john) # Making sure john exists 

    # Now we have to make sure that we are passing in things that sortSingles can take...
    # To do that we need to pass in the formatted version of the data in the collection
    # This should be changed, that way we don't have to create a new dictionary in the backend everytime
    # We only need to pass the reference to the whole data base to the backend

    result = sortSingles.firstSearch(data=formattedData, student=john)  

    # Write the result to a json 
    json_object = json.dumps(formattedData, indent=4)
    with open("result.json", "w") as outfile:
        outfile.write(json_object)
    outfile.close()

    print( "Done Check out output json!" )

