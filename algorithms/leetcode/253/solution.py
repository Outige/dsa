from typing import (
    List,
)

from collections import defaultdict

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def min_meeting_rooms(self, intervals: List[List[int]]) -> int:
        # Edge case: No meetings booked
        if len(intervals) == 0:
            return 0

        # Sort meetings by start times
        intervals.sort(key = lambda interval : interval[0])

        # pass
        endings = defaultdict(int) # key: hour, val: number of meetings ending at that hour
        meeting_pointer = 0
        rooms = 0
        max_rooms = 0
        for i in range(intervals[0][0], intervals[-1][1]+1): # loop for earliest meeting till latest meeting
            # Remove complete meetings
            rooms -= endings[i] # This is bugged if meeting is 0 hours; [0,1] [2,2] [2,3] = 2

            # Add any meeting that is starting at this hour
            # while we have meetings that need rooms still and the current hour is equal to the current meeting's start time
            while meeting_pointer <= len(intervals)-1 and intervals[meeting_pointer][0] == i:
                rooms += 1 # add the current meeting to the current list of rooms required
                endings[intervals[meeting_pointer][1]] += 1 # inc the end count at the time this meeting ends
                meeting_pointer += 1 # point to the next meeting in our intervals
            
            max_rooms = max(max_rooms, rooms)

        return max_rooms


s = Solution()
assert s.min_meeting_rooms([[1,9], [0,8]]) == 2
assert s.min_meeting_rooms([[8,9], [0,8]]) == 1
assert s.min_meeting_rooms([ [8,11], [8,10], [10,11], [9,12], [0,8] ]) == 3
assert s.min_meeting_rooms([ ]) == 0
assert s.min_meeting_rooms([ [0,1], [2,2], [3,4]]) == 1
