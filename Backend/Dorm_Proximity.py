"""
Reasoning/Realization:
So as a ranking from 0-10, each value in each dictionary below is representative of the relative distance that associate dorm is from the any given titular dictionary
The nature of these measurements were made using what Michael and I both deemed to be the two farthest dorms as the ceiling measurement: Bryckwyck to CityStation South/West (~8,976 ft)
Consequently each ranking (sans 0 ofc) is a distributed increment of the ceiling, i.e. 1 <= 897.6 ft; 2 <= 2(897.6 ft); 3 <= 3(897.6 ft) etc.
*NOTE*: 897.6 ft = ~3.4 mins of walking for the average person
What this allows us to do is objectively gauge the distance a student may have to walk from one dorm to the next, allowing for things such as grouping based on proximity from a given "central" dorm
out to others in a set specified vicinity (which a short algorithm below also handles)
"Don't even get me started on the amounts of Google Maps scraping that went into getting this, we're just not going to talk about that rn" --- JG
"""

dorms = ['Barton',	'Bray',	'BarH',	'Cary',	'Crockett',	'Davison',	'E_Complex',	'Hall',	'Nason',	'North',	'Quad',	'Sharp',	'Warren',	'Rahps_B',	'Blitman',	'Bryckwyck',	'Colonie',	'Rahps_A',	'Stacwyck',	'City_Station_West',	'City_Station_South',	'Polytechnic']

Barton_Weights = {	          'Barton' : 0,	'Bray' : 1,	'BarH' : 3,	'Cary' : 1,	'Crockett' : 1,	'Davison' : 1,	'E-Complex' : 2,	'Hall' : 1,	'Nason' : 1,	'North' : 2,	'Quad' : 2,	'Sharp' : 2,	'Warren' : 1,	'Beman and Brinsmade (Rahps B)' : 5,	'Blitman' : 5,	'Bryckwyck' : 6,	'Colonie' : 5,	'Colvin and Albright (Rahps A)' : 3,	'Stacwyck' : 5,	'City Station West' : 6,	'City Station South' : 6,	'Polytechnic' : 5}
Bray_Weights = {	          'Barton' : 1,	'Bray' : 0,	'BarH' : 2,	'Cary' : 1,	'Crockett' : 1,	'Davison' : 1,	'E-Complex' : 3,	'Hall' : 1,	'Nason' : 1,	'North' : 3,	'Quad' : 2,	'Sharp' : 1,	'Warren' : 1,	'Beman and Brinsmade (Rahps B)' : 5,	'Blitman' : 5,	'Bryckwyck' : 6,	'Colonie' : 5,	'Colvin and Albright (Rahps A)' : 3,	'Stacwyck' : 5,	'City Station West' : 6,	'City Station South' : 6,	'Polytechnic' : 5}
BarH_Weights = {	          'Barton' : 3,	'Bray' : 2,	'BarH' : 0,	'Cary' : 3,	'Crockett' : 3,	'Davison' : 3,	'E-Complex' : 3,	'Hall' : 3,	'Nason' : 3,	'North' : 3,	'Quad' : 3,	'Sharp' : 3,	'Warren' : 3,	'Beman and Brinsmade (Rahps B)' : 3,	'Blitman' : 6,	'Bryckwyck' : 4,	'Colonie' : 3,	'Colvin and Albright (Rahps A)' : 1,	'Stacwyck' : 3,	'City Station West' : 8,	'City Station South' : 8,	'Polytechnic' : 6}
Cary_Weights = {	          'Barton' : 1,	'Bray' : 1,	'BarH' : 3,	'Cary' : 0,	'Crockett' : 1,	'Davison' : 1,	'E-Complex' : 3,	'Hall' : 1,	'Nason' : 1,	'North' : 3,	'Quad' : 2,	'Sharp' : 1,	'Warren' : 1,	'Beman and Brinsmade (Rahps B)' : 5,	'Blitman' : 5,	'Bryckwyck' : 6,	'Colonie' : 5,	'Colvin and Albright (Rahps A)' : 3,	'Stacwyck' : 5,	'City Station West' : 6,	'City Station South' : 6,	'Polytechnic' : 5}
Crockett_Weights = {          'Barton' : 1,	'Bray' : 1,	'BarH' : 3,	'Cary' : 1,	'Crockett' : 0,	'Davison' : 1,	'E-Complex' : 3,	'Hall' : 1,	'Nason' : 1,	'North' : 3,	'Quad' : 2,	'Sharp' : 1,	'Warren' : 1,	'Beman and Brinsmade (Rahps B)' : 6,	'Blitman' : 5,	'Bryckwyck' : 6,	'Colonie' : 5,	'Colvin and Albright (Rahps A)' : 3,	'Stacwyck' : 5,	'City Station West' : 6,	'City Station South' : 6,	'Polytechnic' : 5}
Davison_Weights = {	          'Barton' : 1,	'Bray' : 1,	'BarH' : 3,	'Cary' : 1,	'Crockett' : 1,	'Davison' : 0,	'E-Complex' : 3,	'Hall' : 1,	'Nason' : 1,	'North' : 3,	'Quad' : 2,	'Sharp' : 1,	'Warren' : 1,	'Beman and Brinsmade (Rahps B)' : 6,	'Blitman' : 5,	'Bryckwyck' : 6,	'Colonie' : 5,	'Colvin and Albright (Rahps A)' : 3,	'Stacwyck' : 5,	'City Station West' : 5,	'City Station South' : 5,	'Polytechnic' : 5}
E_Complex_Weights = {         'Barton' : 2,	'Bray' : 3,	'BarH' : 3,	'Cary' : 3,	'Crockett' : 3,	'Davison' : 3,	'E-Complex' : 0,	'Hall' : 3,	'Nason' : 3,	'North' : 3,	'Quad' : 1,	'Sharp' : 3,	'Warren' : 3,	'Beman and Brinsmade (Rahps B)' : 6,	'Blitman' : 3,	'Bryckwyck' : 6,	'Colonie' : 6,	'Colvin and Albright (Rahps A)' : 4,	'Stacwyck' : 6,	'City Station West' : 5,	'City Station South' : 5,	'Polytechnic' : 5}
Hall_Weights = {	          'Barton' : 1,	'Bray' : 1,	'BarH' : 3,	'Cary' : 1,	'Crockett' : 1,	'Davison' : 1,	'E-Complex' : 3,	'Hall' : 0,	'Nason' : 1,	'North' : 3,	'Quad' : 2,	'Sharp' : 1,	'Warren' : 1,	'Beman and Brinsmade (Rahps B)' : 6,	'Blitman' : 5,	'Bryckwyck' : 6,	'Colonie' : 5,	'Colvin and Albright (Rahps A)' : 3,	'Stacwyck' : 5,	'City Station West' : 6,	'City Station South' : 6,	'Polytechnic' : 5}
Nason_Weights = {	          'Barton' : 1,	'Bray' : 1,	'BarH' : 3,	'Cary' : 1,	'Crockett' : 1,	'Davison' : 1,	'E-Complex' : 3,	'Hall' : 1,	'Nason' : 0,	'North' : 3,	'Quad' : 2,	'Sharp' : 1,	'Warren' : 1,	'Beman and Brinsmade (Rahps B)' : 6,	'Blitman' : 5,	'Bryckwyck' : 6,	'Colonie' : 5,	'Colvin and Albright (Rahps A)' : 3,	'Stacwyck' : 5,	'City Station West' : 6,	'City Station South' : 6,	'Polytechnic' : 5}
North_Weights = {	          'Barton' : 2,	'Bray' : 3,	'BarH' : 3,	'Cary' : 3,	'Crockett' : 3,	'Davison' : 3,	'E-Complex' : 3,	'Hall' : 3,	'Nason' : 3,	'North' : 0,	'Quad' : 1,	'Sharp' : 3,	'Warren' : 3,	'Beman and Brinsmade (Rahps B)' : 6,	'Blitman' : 3,	'Bryckwyck' : 6,	'Colonie' : 6,	'Colvin and Albright (Rahps A)' : 4,	'Stacwyck' : 6,	'City Station West' : 4,	'City Station South' : 4,	'Polytechnic' : 5}
Quad_Weights = {	          'Barton' : 2,	'Bray' : 2,	'BarH' : 3,	'Cary' : 2,	'Crockett' : 2,	'Davison' : 2,	'E-Complex' : 1,	'Hall' : 2,	'Nason' : 2,	'North' : 1,	'Quad' : 0,	'Sharp' : 2,	'Warren' : 2,	'Beman and Brinsmade (Rahps B)' : 6,	'Blitman' : 4,	'Bryckwyck' : 6,	'Colonie' : 5,	'Colvin and Albright (Rahps A)' : 3,	'Stacwyck' : 5,	'City Station West' : 5,	'City Station South' : 5,	'Polytechnic' : 4}
Sharp_Weights = {	          'Barton' : 2,	'Bray' : 1,	'BarH' : 3,	'Cary' : 1,	'Crockett' : 1,	'Davison' : 1,	'E-Complex' : 3,	'Hall' : 1,	'Nason' : 1,	'North' : 3,	'Quad' : 2,	'Sharp' : 0,	'Warren' : 1,	'Beman and Brinsmade (Rahps B)' : 6,	'Blitman' : 5,	'Bryckwyck' : 6,	'Colonie' : 5,	'Colvin and Albright (Rahps A)' : 4,	'Stacwyck' : 6,	'City Station West' : 5,	'City Station South' : 5,	'Polytechnic' : 4}
Warren_Weights = {	          'Barton' : 1,	'Bray' : 1,	'BarH' : 3,	'Cary' : 1,	'Crockett' : 1,	'Davison' : 1,	'E-Complex' : 3,	'Hall' : 1,	'Nason' : 1,	'North' : 3,	'Quad' : 2,	'Sharp' : 1,	'Warren' : 0,	'Beman and Brinsmade (Rahps B)' : 6,	'Blitman' : 5,	'Bryckwyck' : 6,	'Colonie' : 5,	'Colvin and Albright (Rahps A)' : 3,	'Stacwyck' : 5,	'City Station West' : 6,	'City Station South' : 6,	'Polytechnic' : 5}
Rahps_B_Weights = {        	  'Barton' : 5,	'Bray' : 5,	'BarH' : 3,	'Cary' : 5,	'Crockett' : 6,	'Davison' : 6,	'E-Complex' : 6,	'Hall' : 6,	'Nason' : 6,	'North' : 6,	'Quad' : 6,	'Sharp' : 6,	'Warren' : 6,	'Beman and Brinsmade (Rahps B)' : 0,	'Blitman' : 9,	'Bryckwyck' : 1,	'Colonie' : 3,	'Colvin and Albright (Rahps A)' : 3,	'Stacwyck' : 1,	'City Station West' : 10,	'City Station South' : 10,	'Polytechnic' : 9}
Blitman_Weights = {	          'Barton' : 5,	'Bray' : 5,	'BarH' : 6,	'Cary' : 5,	'Crockett' : 5,	'Davison' : 5,	'E-Complex' : 3,	'Hall' : 5,	'Nason' : 5,	'North' : 3,	'Quad' : 4,	'Sharp' : 5,	'Warren' : 5,	'Beman and Brinsmade (Rahps B)' : 9,	'Blitman' : 0,	'Bryckwyck' : 9,	'Colonie' : 8,	'Colvin and Albright (Rahps A)' : 6,	'Stacwyck' : 8,	'City Station West' : 3,	'City Station South' : 3,	'Polytechnic' : 6}
Bryckwyck_Weights = {         'Barton' : 6,	'Bray' : 6,	'BarH' : 4,	'Cary' : 6,	'Crockett' : 6,	'Davison' : 6,	'E-Complex' : 6,	'Hall' : 6,	'Nason' : 6,	'North' : 6,	'Quad' : 6,	'Sharp' : 6,	'Warren' : 6,	'Beman and Brinsmade (Rahps B)' : 1,	'Blitman' : 9,	'Bryckwyck' : 0,	'Colonie' : 3,	'Colvin and Albright (Rahps A)' : 3,	'Stacwyck' : 1,	'City Station West' : 10,	'City Station South' : 10,	'Polytechnic' : 10}
Colonie_Weights = {	          'Barton' : 5,	'Bray' : 5,	'BarH' : 3,	'Cary' : 5,	'Crockett' : 5,	'Davison' : 5,	'E-Complex' : 6,	'Hall' : 5,	'Nason' : 5,	'North' : 6,	'Quad' : 5,	'Sharp' : 5,	'Warren' : 5,	'Beman and Brinsmade (Rahps B)' : 3,	'Blitman' : 8,	'Bryckwyck' : 3,	'Colonie' : 0,	'Colvin and Albright (Rahps A)' : 3,	'Stacwyck' : 3,	'City Station West' : 9,	'City Station South' : 9,	'Polytechnic' : 9}
Rahps_A_Weights = {        	  'Barton' : 3,	'Bray' : 3,	'BarH' : 1,	'Cary' : 3,	'Crockett' : 3,	'Davison' : 3,	'E-Complex' : 4,	'Hall' : 3,	'Nason' : 3,	'North' : 4,	'Quad' : 3,	'Sharp' : 4,	'Warren' : 3,	'Beman and Brinsmade (Rahps B)' : 3,	'Blitman' : 6,	'Bryckwyck' : 3,	'Colonie' : 3,	'Colvin and Albright (Rahps A)' : 0,	'Stacwyck' : 3,	'City Station West' : 8,	'City Station South' : 8,	'Polytechnic' : 8}
Stacwyck_Weights = {	      'Barton' : 5,	'Bray' : 5,	'BarH' : 3,	'Cary' : 5,	'Crockett' : 5,	'Davison' : 5,	'E-Complex' : 6,	'Hall' : 5,	'Nason' : 5,	'North' : 6,	'Quad' : 5,	'Sharp' : 6,	'Warren' : 5,	'Beman and Brinsmade (Rahps B)' : 1,	'Blitman' : 8,	'Bryckwyck' : 1,	'Colonie' : 3,	'Colvin and Albright (Rahps A)' : 3,	'Stacwyck' : 0,	'City Station West' : 10,	'City Station South' : 10,	'Polytechnic' : 9}
City_Station_West_Weights = { 'Barton' : 6,	'Bray' : 6,	'BarH' : 8,	'Cary' : 6,	'Crockett' : 6,	'Davison' : 5,	'E-Complex' : 5,	'Hall' : 6,	'Nason' : 6,	'North' : 4,	'Quad' : 5,	'Sharp' : 5,	'Warren' : 6,	'Beman and Brinsmade (Rahps B)' : 10,	'Blitman' : 3,	'Bryckwyck' : 10,	'Colonie' : 9,	'Colvin and Albright (Rahps A)' : 8,	'Stacwyck' : 10,'City Station West' : 0,	'City Station South' : 1,	'Polytechnic' : 5}
City_Station_South_Weights = {'Barton' : 6,	'Bray' : 6,	'BarH' : 8,	'Cary' : 6,	'Crockett' : 6,	'Davison' : 5,	'E-Complex' : 5,	'Hall' : 6,	'Nason' : 6,	'North' : 4,	'Quad' : 5,	'Sharp' : 5,	'Warren' : 6,	'Beman and Brinsmade (Rahps B)' : 10,	'Blitman' : 3,	'Bryckwyck' : 10,	'Colonie' : 9,	'Colvin and Albright (Rahps A)' : 8,	'Stacwyck' : 10,'City Station West' : 1,	'City Station South' : 0,	'Polytechnic' : 5}
Polytechnic_Weights = {       'Barton' : 5,	'Bray' : 5,	'BarH' : 6,	'Cary' : 5,	'Crockett' : 5,	'Davison' : 5,	'E-Complex' : 5,	'Hall' : 5,	'Nason' : 5,	'North' : 5,	'Quad' : 4,	'Sharp' : 4,	'Warren' : 5,	'Beman and Brinsmade (Rahps B)' : 9,	'Blitman' : 6,	'Bryckwyck' : 10,	'Colonie' : 9,	'Colvin and Albright (Rahps A)' : 8,	'Stacwyck' : 9,	'City Station West' : 5,	'City Station South' : 5,	'Polytechnic' : 0}

# Returns the value pertaining some key (LocB) in a passed dict (LocA)
def Dist_Rating(LocA, LocB):
    assert isinstance(LocA, dict)
    assert isinstance(LocB, str)

    return LocA[LocB]

# returns a set of dorms distant from Loc that fit a passed rating or rating range (inclusive)
def Relative_Proximity(Loc, Rating_range):
    assert isinstance(Loc, dict)

    if isinstance(Rating_range, int):
        return [k for k,v in Loc.items() if int(v) == Rating_range]
    if isinstance(Rating_range, list):
        return sorted([(v,k) for k,v in Loc.items() if int(v) >= Rating_range[0] and int(v)<=Rating_range[-1]])
    else:
        return "Error: Rating range is invalid."

# returns a set of dorms relatively equidistant from the locations (dicts) passed as an array to Loc_set, left out for now
def Proximity_grouping(Loc_set, Rating_range):
    pass

if __name__ == "__main__":
    #syntactical example(s)
    print(Dist_Rating(BarH_Weights,"E-Complex"))
    print()
    print(Relative_Proximity(Polytechnic_Weights,[5,7]))
    print()
    print(Relative_Proximity(Barton_Weights,[1,3]))