"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 0 or len(intervals) == 1:
            return True

        intervals.sort(key=lambda x: x.start)

        currs, curre = intervals[0].start, intervals[0].end
        for i in range(1, len(intervals)):
            start, end = intervals[i].start, intervals[i].end

            if start < curre:
                return False

            currs = start
            curre = end

        return True
            
