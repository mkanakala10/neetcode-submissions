"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals = sorted(intervals, key = lambda x : x.start)
        heap = [intervals[0].end]
        prev = -1
        room = 1

        for i in range(1, len(intervals)):
            curr = heapq.heappop(heap)
            if intervals[i].start < curr:
                room += 1
                heapq.heappush(heap, curr)
            heapq.heappush(heap, intervals[i].end)

        return room
            