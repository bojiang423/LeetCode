## Insert Interval
'''
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Example 3:
Input: intervals = [], newInterval = [2,5]
Output: [[2,5]]

Example 4:
Input: intervals = [[1,5]], newInterval = [2,3]
Output: [[1,5]]
'''

#########################################################
# my solution                                           #
# 154 / 154 test cases passed.                          #
# Runtime: 76 ms (> 95.55%)                             #
# Memory Usage: 17.1 MB (>71.75)                        #
#########################################################
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        result = []
        
        if len(intervals) == 0:
            result.append(newInterval)
            return result
        
        midIntervalAdded = False
        midInterval = newInterval
        for interval in intervals:
            #print(f'current interval[{interval[0]},{interval[1]}], added {midIntervalAdded}')
            #print(f'middle  interval[{midInterval[0]},{midInterval[1]}]')
            if midIntervalAdded:
                result.append(interval)
            else:
                if interval[1] < midInterval[0]:  # no overlap, just append the smaller interval
                    result.append(interval)
                elif interval[0] < midInterval[0]:
                    midInterval[0] = interval[0]
                    if interval[1] < midInterval[1]:
                        continue
                    else:
                        midInterval[1] = interval[1]
                elif interval[0] > midInterval[1]:
                    result.append(midInterval)
                    result.append(interval)
                    midIntervalAdded = True
                elif interval[0] >= midInterval[0]:
                    if interval[1] < midInterval[1]:
                        continue
                    else:
                        midInterval[1] = interval[1]
        if not midIntervalAdded:
            result.append(midInterval)
                    
        return result

#########################################################
# fastest solution (60 ms)                              #
#########################################################
'''
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        found = False
        for i in range(len(intervals)):
            if intervals[i][0] > newInterval[0]:
                intervals = intervals[:i] + [newInterval] + intervals[i:]
                found = True
                break
        
        if not found:
            intervals.append(newInterval)
        
        merged = []
        for interval in intervals:
            if len(merged) != 0 and merged[-1][1] >= interval[0]:
                merged[-1][1] = max(merged[-1][1], interval[1])
            else:
                merged.append(interval)
        
        return merged
'''

#########################################################
# fastest solution (64 ms)                              #
#########################################################
'''
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start, end = newInterval[0], newInterval[-1]
        left, right = [], []
        
        for interval in intervals:
            if interval[-1] < start:
                left += interval,
            elif interval[0] > end:
                right += interval,
            else:
                start = min(start, interval[0])
                end = max(end, interval[-1])
                
        print(type([left]))
        print(right)
        rtn = []
        rtn.extend(left)
        rtn.append([start, end])
        rtn.extend(right)
        return rtn
'''