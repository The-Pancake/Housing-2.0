# Implement Algorithm Here:
#adds occupants to room if the group fits the size
def bestSearch(group,campus):
    with open(group, 'r') as f1, open(campus, 'r') as f2:
    group_data = json.load(f1)
    room_data = json.load(f2)
    
# Iterate through the rooms in the second JSON file
    for room_name, room_info in room_data.items():
        room_size = room_info['size']
        occupants = room_info['Occupants']
    
    # Check if the size of the group matches the size of the room
    for group_name, group_info in group_data.items():
        group_size = len(group_info['group'])
        if group_size == room_size:
            occupants.append(group_name)

    # Update the Occupants list of the room in the second JSON file
    room_data[room_name]['Occupants'] = occupants

    # Save the updated second JSON file
    with open(campus, 'w') as f:
        json.dump(room_data, f, indent=4)
    return
