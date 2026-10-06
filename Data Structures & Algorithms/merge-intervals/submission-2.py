class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        if not intervals:
            return res
        intervals.sort(key = lambda x : x[0])
        res.append(intervals[0])
        for i in range(1, len(intervals)):
            start, end = res.pop()
            if end >= intervals[i][0]:
                res.append([start, max(end, intervals[i][1])])
            else:
                res.append([start, end])
                res.append(intervals[i])

        return res