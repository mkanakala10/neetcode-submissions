class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_max = float('-inf')
        max_now = 0
        for i in nums:
            max_now = max_now + i
            if max_now > curr_max:
                curr_max = max_now
            if max_now < 0:
                max_now = 0
        return curr_max