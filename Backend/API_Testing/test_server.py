import requests
import json

if __name__ == "__main__": 

    # # Grab from server 
    # students = requests.get("http://127.0.0.1:8000/students/").json()

    # # Printing the students out 
    # print(students)

    print(requests.get("http://127.0.0.1:8000/students/").json())