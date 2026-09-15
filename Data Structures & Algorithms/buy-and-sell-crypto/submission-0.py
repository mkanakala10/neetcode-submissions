class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprof = 0
        low = prices[0]
        for i in prices:
            if i < low:
                low = i
            maxprof = max(maxprof, i - low)
        return maxprof