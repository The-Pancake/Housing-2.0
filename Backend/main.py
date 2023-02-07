import json
import sort

if __name__ == "__main__":
    
    with open("test.json") as json_file:
        data = json.load(json_file)

    with open("1.json") as json_file:
        t1 = json.load(json_file)
    with open("2.json") as json_file:
        t2 = json.load(json_file)

    print(sort.sortFucntion(data, t1))
    print(sort.sortFucntion(data, t2))

    with open("test.json", "w") as out:
        json.dump(data, out, indent=4)
    