# goals for the moment:
# get a baseline working with limited students and housing
# up the scale slowly and compare data structues with whatever else people write

import json
import sort
import random

if __name__ == "__main__":
    
    with open("test.json") as json_file:
        data = json.load(json_file)

    with open("1.json") as json_file:
        t1 = json.load(json_file)
    with open("2.json") as json_file:
        t2 = json.load(json_file)
    with open("3.json") as json_file:
        t3 = json.load(json_file)
    with open("4.json") as json_file:
        t4 = json.load(json_file)
    with open("5.json") as json_file:
        t5 = json.load(json_file)

    print(sort.firstSearch(data, t1))
    print(sort.firstSearch(data, t2))
    print(sort.firstSearch(data, t3))
    print(sort.firstSearch(data, t4))
    print(sort.firstSearch(data, t5))

    with open("names.json") as json_file:
        names = json.load(json_file)
    with open("states.json") as json_file:
        states = json.load(json_file)
    with open("majors.json") as json_file:
        majors = json.load(json_file)
    
    s = ["m", "f"]
    
    for i in range(200):
        
        name = names[random.randrange(0, len(names))]
        sex = s[random.randrange(0, 2)]
        major = majors[random.randrange(0, len(majors))]
        state = states[random.randrange(0, len(states))]

        randStudent = {
            "name": name,
            "sex": sex,
            "major": major,
            "dormPref": "",
            "year": "freshman",
            "geo": state
        }

        #print(sort.firstSearch(data, randStudent))

    with open("test.json", "w") as out:
        json.dump(data, out, indent=4)
    