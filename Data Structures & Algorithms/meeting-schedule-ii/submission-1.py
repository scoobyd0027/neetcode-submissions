"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        q = []
        intervals.sort(key = lambda x: (x.start, x.end))
        for interval in intervals:
            s, e = interval.start, interval.end
            if q and q[0] <= s:
                heapq.heappop(q)
            
            heapq.heappush(q, e)
        return len(q)
