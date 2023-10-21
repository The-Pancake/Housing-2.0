import requests
import sys 
import os 
import json 

dir = os.path.dirname(os.path.realpath("../Backend"))
sys.path.append(dir)

import sortSingles

if __name__ == "__main__": 
    
    dormData = open('/home/beef-patty/Desktop/Housing2.0_Fall_2023/Housing-2.0/Backend/test.json', 'r')

    print( json.dumps(json.load(dormData), indent=2) )
    john = requests.get("http://127.0.0.1:5000/students/0/").json()

    sortSingles.firstSearch()
    dormData.close()