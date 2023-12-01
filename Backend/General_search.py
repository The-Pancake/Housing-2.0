from pymongo import MongoClient

def connect_to_db(uri):
    """
    Connects to the MongoDB database using the provided URI.

    Args:
    - uri (str): The MongoDB connection string URI.

    Returns:
    - db: A database object representing the 'Campus' database.

    This function creates a MongoClient with the given URI, then selects and returns 
    the 'Campus' database. Note that the database name should be replaced with the actual 
    name of your database.
    """
    client = MongoClient(uri)
    db = client['Campus']  
    return db

def findAvailableRoom(db, groupSize, students):
    """
    Searches for an available room in the dormitory that can accommodate a group of a given size.

    Args:
    - db: The database object to perform queries on.
    - groupSize (int): The number of students in the group.
    - students (list): List of student names to be added to the room.

    Returns:
    - tuple: (status, room_info) where 'status' is a boolean indicating if a room was found,
             and 'room_info' is a string describing the found room or None if no room is found.

    This function queries the 'Dorms_Rohan' collection in the database to find a room 
    that is currently empty (no occupants) and can accommodate the specified group size.
    If such a room is found, it updates the 'Occupants' field with the students' names
    and returns the room information.
    """
    # Query to find a room with empty occupants and sufficient size
    potential_room = db['Dorms_Rohan'].find_one({
        "Occupants": [],
        "Size": {"$gte": groupSize}
    })
    
    if potential_room:
        # Building the room information string
        hall = potential_room["Dorm"]
        room_info = hall + " " + str(potential_room["RoomNum"])
        
        # Update the room occupants in MongoDB.
        db['Dorms_Rohan'].update_one({"_id": potential_room["_id"]}, {"$set": {"Occupants": students}})
        return True, room_info
    
    return False, None

def printData(db):
    """
    Prints details of all dorm rooms in the 'Dorms_Rohan' collection.

    Args:
    - db: The database object to perform queries on.

    This function retrieves and prints detailed information about each dorm room 
    in the 'Dorms_Rohan' collection, including the room number, size, bathroom sharing status, 
    type, and current occupants.
    """
    dorms = db['Dorms_Rohan'].find()
    for dorm in dorms:
        print(dorm["Dorm"], ":")
        print("  ", dorm["RoomNum"], ":")
        print("    room size:", dorm["Size"])
        print("    shared bathroom:", dorm["sharedBathroom"])
        print("    type:", dorm["type"])
        print("    occupants:")
        for occupant in dorm["Occupants"]:
            print("\t", occupant)

# Connection URI
uri = "mongodb+srv://housing20rcos:nQWnpyw4PsFk78eJ@housing2.elxx6hn.mongodb.net/?retryWrites=true&w=majority"

# Connect to MongoDB
try:
    db = connect_to_db(uri)
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    exit()

# Example usage of the functions
students = ["John", "Bill"]
groupSize = len(students)

room_found, given_room = findAvailableRoom(db, groupSize, students)

if room_found:
    print("Room found:", given_room)
else:
    print("No suitable room found for the group.")

printData(db)






