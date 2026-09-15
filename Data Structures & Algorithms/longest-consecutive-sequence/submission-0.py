class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        for i in nums:
            if (i - 1) not in nums:
                maxlength = 1
                while (i + maxlength) in nums:
                    maxlength += 1
                longest = max(maxlength, longest)
        return longest