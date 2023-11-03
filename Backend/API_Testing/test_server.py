import requests
import sys
import json 
import uvicorn

sys.path.append('/home/beef-patty/Desktop/Housing2.0_Fall_2023/Housing-2.0/Backend')
sys.path.append('/home/beef-patty/Desktop/Housing2.0_Fall_2023/Housing-2.0/Backend/Database/dorm_data')

import sortSingles
import mongodb_test as mb

if __name__ == "__main__": 
    

    # Grab a student from the front end
    john = requests.get("http://127.0.0.1:8000/students/0/").json()

    
    # Grab dorm information from backend 
    database = mb.connect_to_database("Campus")
    collection = database["Dorms_Daniel"]
    data = mb.get_all_data(collection)


    # Testing it by printing it all out.
    for item in data: 
        print(item)