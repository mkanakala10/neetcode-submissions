class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        if not intervals:
            return count
        res = []
        
        
        intervals.sort(key=lambda x : x[0])
        res.append(intervals[0])

        overlaps = {}

        for i in range(1, len(intervals)):
            start, end = res.pop()
            if end > intervals[i][0]:
                if end >= intervals[i][1]:
                    res.append(intervals[i])
                else:
                    res.append([start, end])
                count += 1
            else:
                res.append([start, end])
                res.append(intervals[i])
        return count