class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        themap = {}
        for i in nums:
            if i in themap:
                themap[i] += 1
            else:
                themap[i] = 1
        result = sorted(themap, key = themap.get, reverse =True)
        return result[:k]