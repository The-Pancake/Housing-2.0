#   _   _   _   _   _   _   _   _   _   _  
#  / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ 
# ( H | o | u | s | i | n | g | 2 | . | 0 )
#  \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ 
#

# Author: Daniel 
#
# Description:
# The following python code sends to the database a sample quiz structure
# that will be stored in the backend. The frontend will ask a student to 
# complete a "compatibility" quiz so that the backend algorithms could try to
# match students to their best locations on campus. After the quiz is complete 
# the student's rcsid and quiz will be sent to the backend


import sys
sys.path.append('/home/beef-patty/Desktop/Housing2.0_Fall_2023/Housing-2.0/Backend/Database')

from dorm_data import mongodb_test as mb

if __name__ == "__main__":
    # Let's connect to the data base
    db = mb.connect_to_database("Student_Info")
    collection = db["Quiz"]
    
    # Delete everything from collection: 
    collection.delete_many({})

    # Sending Quiz sample to Quiz collection ....
    # First create dictionary for this: 
    # Note: Each question will have a sample weight 
    quiz_sample = {
           
        "RCSID": 123151312 ,

        "question1" : {
            "prompt" : "What's your preferred sleeping schedule? [Time you go to bed, Time you wake up]", 
            "choices" : None, 
            "answer" : None,
            "weight" : 2
        },

        "question2" : {
            "prompt" : "How tidy are you in your living space?",
            "choices" : ["Very Tidy", "Somewhat Tidy", "Not really..."],
            "answer" : None,
            "weight" : 3
        },
        
        "question3" : {
            "prompt" : "Do you have any allergies?",
            "choices" : None, 
            "answer" : None, 
            "weight" : 4
        },

        "question4" : {
            "prompt" : "Are you interested in sharing personal belonings like a TV \
                        or kitchen appliances with your roommate?",
            "choices" : ["yes", "no"], 
            "answer" : None, 
            "weight" : 4
        },
        
        "question5" : {
            "prompt" : "What are some of you hobbies?",
            "choices" : [ "Reading", "Gaming", "Cooking", "Hiking", "Sports", "Instrument", "Writing", 
                        "Artistry", "Table Top Games", "Photography", "Cycling", "Fishing", "Singing", "Dancing"],
            "answer" : None, 
            "weight" : 5
        },
    
        "question6" : {
            "prompt" : "What's your major?",
            "choices" : [ "Game and Interactive Media Design", "Music Theory and Composition", 
                        "Visual and Performing Arts, General", "Business Administration and Management, General", 
                        "Economics, General", "Cognitive Science", "Pre-Medicine/Pre-Medical Studies", 
                        "Communication Studies/Speech Communication and Rhetoric", "Communication, General", 
                        "Digital Communication and Media/Multimedia", "Philosophy", "Computer Technology/Computer Systems Technology", 
                        "Multi-/Interdisciplinary Studies, General", "Multi-/Interdisciplinary Studies, Other", 
                        "Aerospace, Aeronautical and Astronautical Engineering", "Architecture", 
                        "Biochemistry, Biophysics and Molecular Biology, Other", "Biochemistry/Biophysics and Molecular Biology", 
                        "Bioinformatics", "Biological and Biomedical Sciences, Other", "Biology/Biological Sciences, General",
                        "Biomedical/Medical Engineering", "Chemical Engineering", "Chemistry, General", "Civil Engineering, General", 
                        "Computer Science", "Computer and Information Sciences, General", "Electrical, Electronics and Communications Engineering", 
                        "Engineering Physics", "Engineering Science", "Environmental Science", "Environmental/Environmental Health Engineering", 
                        "Geology/Earth Science, General", "Hydrology and Water Resources Science", "Industrial Engineering", "Information Technology", 
                        "Materials Engineering", "Mathematics, General", "Mechanical Engineering", "Nuclear Engineering", "Physical Sciences, Other", 
                        "Physics, General", "Physics, Other", "Psychology, General", "Science, Technology and Society", "Social Sciences, General"
                        ],
            "answer" : None,
            "weight" : 5
        },

        
        "question7" : {
            "prompt" : "What music suits your tastes best?", 
            "choices" : ["Pop", "Rock", "Classical", "Jazz", "Indie", "Country/Folk",
                        "K-Pop", "Metal/Grunge", "Electronic", "Country", "Hip-Hop" ],
            "answer" : None, 
            "weight" : 5 
        },

        # This needs to be modified to account for international students ... 
        "question8" : {
            "prompt" : "Where are you from?",
            "choices" : [ "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA",	
                        "HI","ID","IL",	"IN","IA","KS",	"KY", "LA", "ME", "MD",	"MA",	
                        "MI", "MN",	"MS","MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY",	
                        "NC", "ND",	"OH", "OK",	"OR", "PA",	"RI", "SC",	"SD", "TN",	"TX",	
                        "UT", "VT",	"VA", "WA",	"WV", "WI",	"WY", "International"],
            "answer": None,
            "weight": 5
        },

        # This should be different depending on student year ... 
        
        "question9" : {
            "prompt" : "What's your preferred dorm? (If you have any)",
            "choices" : ["Crockett Hall, Barton Hall, North Hall, Hall Hall, Bar-H, Warren Hall"],
            "answer" : None,
            "weight": 1
        
        },

        "question10" : {
            "prompt" : "What's your ideal noise level in your living space?",
            "choices" : ["Quiet please!", "Moderate noise is fine", "I don't mind some loud music or chatter"],
            "answer" :  None,
            "weight": 3
        }    
    }   

    print("Sending Quiz To Backend ..... ")
    
    # Store the students quiz answers as one object: 
    collection.insert_one(quiz_sample)
    
    print("Complete!")


