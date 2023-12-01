from pymongo import MongoClient

def connect_to_db(uri):
    """
    Connects to the MongoDB database using the provided URI.

    Args:
    - uri (str): The MongoDB connection string URI.

    Returns:
    - db: A database object representing the 'Campus' database.

    This function establishes a connection to the MongoDB database specified by the URI.
    It then selects the 'Campus' database and returns it for further operations.
    """
    client = MongoClient(uri)
    db = client['Campus'] 
    return db

def searchIdeal(db, groupSize, preferred, students):
    """
    Searches for an ideal dorm room based on preferences and group size.

    Args:
    - db: The database object to perform queries on.
    - groupSize (int): The size of the student group.
    - preferred (list): A list of preferred dorm names.
    - students (list): A list of students to be added as occupants.

    Returns:
    - tuple: (status, message) where 'status' is a boolean indicating if a suitable room was found,
             and 'message' is a string describing the room or None if no room is found.

    This function iterates through the preferred dorm list. For each preferred dorm, 
    it queries the 'Dorms_Rohan' collection in the database to find an available room that
    can accommodate the specified group size and has no current occupants.
    If such a room is found, it updates the room's 'Occupants' field with the list of students,
    and returns a success status along with the dorm name and room number.
    """
    for pref in preferred:
        # Query to find rooms with enough space and empty Occupants array
        room = db['Dorms_Rohan'].find_one({
            "Dorm": pref, 
            "Size": {"$gte": groupSize}, 
            "Occupants": []
        })

        if room:
            # Update the room occupants in MongoDB
            db['Dorms_Rohan'].update_one({"_id": room["_id"]}, {"$set": {"Occupants": students}})
            return True, f"{pref} Room {room['RoomNum']}"  # Return the dorm name and room number
    return False, None

# Connection URI
uri = "mongodb+srv://housing20rcos:nQWnpyw4PsFk78eJ@housing2.elxx6hn.mongodb.net/?retryWrites=true&w=majority"

# Connect to MongoDB
try:
    db = connect_to_db(uri)
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    exit()
