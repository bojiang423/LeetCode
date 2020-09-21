# Car Pooling

'''
You are driving a vehicle that has capacity empty seats initially available for passengers.  
The vehicle only drives east (ie. it cannot turn around and drive west.)

Given a list of trips, trip[i] = [num_passengers, start_location, end_location] contains information about the i-th trip: 
the number of passengers that must be picked up, and the locations to pick them up and drop them off.  
The locations are given as the number of kilometers due east from your vehicle's initial location.

Return true if and only if it is possible to pick up and drop off all passengers for all the given trips. 

Constraints:
- trips.length <= 1000
- trips[i].length == 3
- 1 <= trips[i][0] <= 100
- 0 <= trips[i][1] < trips[i][2] <= 1000
- 1 <= capacity <= 100000

'''

#################################################################
# My solution 1 
# 54 / 54 test cases passed.
# Status: Accepted
# Runtime: 480 ms
# Memory Usage: 14.3 MB
#################################################################
def carPooling(trips, capacity):

    stop_cap = {}

    for trip in trips:
        for i in range(trip[1], trip[2]):
            if i in stop_cap:
                stop_cap[i] = stop_cap[i] + trip[0]
            else:
                stop_cap[i] = trip[0]

            if stop_cap[i] > capacity:
                return False
    
    return True


trips_01 = [[2,1,5],[3,3,7]]
capacity_01 = 4
expected_01 = False

trips_02 = [[2,1,5],[3,3,7]]
capacity_02 = 5
expected_02 = True

trips_03 = [[2,1,5],[3,5,7]]
capacity_03 = 3
expected_03 = True

trips_04 = [[3,2,7],[3,7,9],[8,3,9]]
capacity_04 = 11
expected_04 = True


print(f'{carPooling(trips_04, capacity_04)}')

#################################################################
# Fastest solution (48ms)
#################################################################
'''
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        pois = []
        for num, start, end in trips:
            pois.extend([(start, num), (end, -num)])
        num_used = 0
        for _, num in sorted(pois):
            num_used += num
            if num_used > capacity:
                return False
        return True
'''