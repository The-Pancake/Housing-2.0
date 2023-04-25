"""
This might be too excessive too implement, so we will talk about this one at a later date as we progress with project

Ideal Near Building Search:
Note: Under some off chance happening, maybe a group of 4 can not be in a group and must break up into 2 smaller groups

Task:
Create an algorithm that takes 2 pairs and tries to find the nearest 2 buildings that has rooms for each pair to reside in.

(Things to keep in mind: Would there be a better way to implement this or this too niche to be implemented)
"""
import names 
import sys
import random
from Dorm_Proximity import *

years = ["Freshman", "Sophmore", "Junior","Senior"]
majors = [
    "Game and Interactive Media Design",
    "Music Theory and Composition",
    "Visual and Performing Arts, General",
    "Business Administration and Management, General",
    "Economics, General",
    "Cognitive Science",
    "Pre-Medicine/Pre-Medical Studies",
    "Communication Studies/Speech Communication and Rhetoric",
    "Communication, General",
    "Digital Communication and Media/Multimedia",
    "Philosophy",
    "Computer Technology/Computer Systems Technology",
    "Multi-/Interdisciplinary Studies, General",
    "Multi-/Interdisciplinary Studies, Other",
    "Aerospace, Aeronautical and Astronautical Engineering",
    "Architecture",
    "Biochemistry, Biophysics and Molecular Biology, Other",
    "Biochemistry/Biophysics and Molecular Biology",
    "Bioinformatics",
    "Biological and Biomedical Sciences, Other",
    "Biology/Biological Sciences, General",
    "Biomedical/Medical Engineering",
    "Chemical Engineering",
    "Chemistry, General",
    "Civil Engineering, General",
    "Computer Science",
    "Computer and Information Sciences, General",
    "Electrical, Electronics and Communications Engineering",
    "Engineering Physics",
    "Engineering Science",
    "Environmental Science",
    "Environmental/Environmental Health Engineering",
    "Geology/Earth Science, General",
    "Hydrology and Water Resources Science",
    "Industrial Engineering",
    "Information Technology",
    "Materials Engineering",
    "Mathematics, General",
    "Mechanical Engineering",
    "Nuclear Engineering",
    "Physical Sciences, Other",
    "Physics, General",
    "Physics, Other",
    "Psychology, General",
    "Science, Technology and Society",
    "Social Sciences, General"
]
states = [ 'AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
           'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME',
           'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM',
           'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX',
           'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']
def gen_rand_students(num):
    students = []
    for i in range(num):
        data = {}
        sex = random.randint(1, 2)
        if sex == 1:
            data['Name'] = names.get_full_name(gender='male')
            data['Sex'] = 'male'
        else:
            data['Name'] = names.get_full_name(gender='female')
            data['sex'] = 'female'
        data['Major'] = random.choice(majors)
        data['Dorm_Pref'] = random.choice(dorms)
        data['Dorm'] = ""
        data['Year'] = random.choice(years)
        data['Year'] = random.choice(states)
        students.append(data)
    return students

count_of_quads  = int(sys.argv[1]) * 4
students = gen_rand_students(count_of_quads)
group = []
for i in range(count_of_quads):

    group.append(students[i]["Dorm_Pref"])

    if (i+1)%4==0:
        print("\n")
        print("#"*150)
        print(group)
        print("***Dorms in relative proximity range of 1-3 from " + group[0] + " and " + group[1] + "***:")
        print()
        print(group[0] +": ")
        vicins = [Relative_Proximity(locals()[group[0]+"_Weights"],[1,3]), Relative_Proximity(locals()[group[1]+"_Weights"],[1,3]),Relative_Proximity(locals()[group[2]+"_Weights"],[1,3]),Relative_Proximity(locals()[group[3]+"_Weights"],[1,3])]
        print(vicins[0])
        print(group[1] +": ")
        print(vicins[1])
        matches = [dorm1 for (ratings1,dorm1) in vicins[0]
        for (ratings2,dorm2) in vicins[1] if dorm1 == dorm2]
        print("**Search_matches**: "+ str(matches))
        print("")

        print(group[2] +": ")
        print(vicins[2])
        print(group[3] +": ")
        print(vicins[3])

        group = []