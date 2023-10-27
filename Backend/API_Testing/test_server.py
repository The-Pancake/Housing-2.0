import requests
import sys
import json 

sys.path.append('/home/beef-patty/Desktop/Housing2.0_Fall_2023/Housing-2.0/Backend')
sys.path.append('/home/beef-patty/Desktop/Housing2.0_Fall_2023/Housing-2.0/Backend/Database')

import sortSingles
import mongodb_test as db


uri = "mongodb+srv://housing20rcos:nQWnpyw4PsFk78eJ@housing2.elxx6hn.mongodb.net/?retryWrites=true&w=majority"

if __name__ == "__main__": 
    
    
    john = requests.get("http://127.0.0.1:8000/students/0/").json()

    # Grab dorm information from backend 
    database = db.connect_to_database(uri, "Campus")
    collection = database["Dorms_Daniel"]
    data = db.get_all_data(collection)

    # Testing it by printing it all out.
    for item in data: 
        print(item)