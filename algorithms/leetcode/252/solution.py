from typing import (
    List,
)

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
    def can_attend_meetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key = lambda interval : interval[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                return False
        return True

s = Solution()
assert s.can_attend_meetings([[1,9], [0,8]]) == False
assert s.can_attend_meetings([[8,9], [0,8]]) == True
assert s.can_attend_meetings([[8,11], [0,8], [9,12]]) == False




"""
Sorting of various structures
"""
class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __str__(self):
        return f'[{self.start}, {self.end}]'
    
    def __repr__(self):
        return self.__str__()

intervals = [Interval(9, 11), Interval(0, 9), Interval(11, 12)]
intervals.sort(key = lambda interval : interval.start)
print(intervals)

intervals = [{'start': 9, 'end': 11}, {'start': 0, 'end': 9}, {'start': 11, 'end': 12}]
intervals.sort(key = lambda interval : interval['start'])
print(intervals)
