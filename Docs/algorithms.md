# Algorithm Information
This document contains information regarding algorithms used for assigning students their rooms

## Algorithms
The following algorithms are used in determining a student or a group of students' rooms that they will be assigned.<br>
- Singles Search
- Ideal/General Search
- Ideal/General Split Search
- Ideal/General Near Search
- Near Building Search

All algorithms after Ideal/General Search will split the group up into two groups since failing the Ideal/General search means the algorithm could not find any room to assign the group and must make the group smaller to have a better chance to put them into a smaller room.

### Ideal vs General Algorithms
`Ideal algorithms` attempt to put students/groups into the dorm that falls into their preferred dorm list<br>
`General algorithms` attmpt to put students/groups into any dorm that fits them

### Singles Search

### Ideal/General Search

### Ideal/General Split Search
Split Search splits the group up into two subgroups and attempts to find two dorm rooms that are connected via a bathroom and checks if there is space in both rooms to put both subgroups<br>
If two connected rooms are found, the algorithm updates the database by populating the room's data with the subgroups' data and returns `TRUE` to indicate that rooms were found, `FALSE` if no rooms were found.

### Ideal/General Near Search
Near Search splits the group up into two subgroups and attempts to find two dorm rooms that are within the same dorm and checks if there is space in both rooms to put both subgroups<br>
If two rooms are found, the algorithm updates the database by populating the room's data with the subgroups' data and returns `TRUE` to indicate that possible rooms were found, `FALSE` if no rooms were found.

### Near Building Search
