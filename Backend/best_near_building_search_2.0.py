def find_nearest_buildings(data, group1_pref, group2_pref):
    # Initialize the nearest building pair to None and set the minimum distance to infinity.
    nearest_building_pair = None
    min_distance = float('inf')
    
    # Iterate through each building preference of group 1
    for building1 in group1_pref:
        # Iterate through each building preference of group 2
        for building2 in group2_pref:
            # Create weight keys based on the building names
            weight_key1 = building1 + "_Weights"
            weight_key2 = building2 + "_Weights"
            
            # Check if the weight keys exist in global variables
            if weight_key1 in globals() and weight_key2 in globals():
                # Calculate the relative distance between the two buildings using a function named Dist_Rating
                # The function presumably takes in two arguments: weight and building name
                distance = Dist_Rating(globals()[weight_key1], building2) + Dist_Rating(globals()[weight_key2], building1)
                
                # Update the nearest building pair if this distance is shorter than the previously recorded minimum distance
                if distance < min_distance:
                    min_distance = distance
                    nearest_building_pair = (building1, building2)

    # Return the nearest building pair
    return nearest_building_pair

