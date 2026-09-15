class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        premap = {}
        for i, n in enumerate(nums):
            difference = target - n
            if difference in premap:
                return [premap[difference], i]
            premap[n] = i