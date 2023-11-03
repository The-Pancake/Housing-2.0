#   _   _   _   _   _   _   _   _   _   _  
#  / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ 
# ( H | o | u | s | i | n | g | 2 | . | 0 )
#  \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ 
#

# Author: Daniel 
#
# Description:

import mongodb_test as mb
import json

if __name__ == "__main__":
    # Connect to database
    db = mb.connect_to_database("Campus")
    collection = db["Dorms_Daniel"]
    
    # Delete everything from collection: 
    collection.delete_many({})

    newDorm = json.load(open("crockett.json"))
    
    # Populate with updated json file
    collection.insert_many(newDorm)