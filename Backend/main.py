# goals for the moment:
# get a baseline working with limited students and housing
# up the scale slowly and compare data structues with whatever else people write

import json
import sort

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

    with open("test.json", "w") as out:
        json.dump(data, out, indent=4)
    