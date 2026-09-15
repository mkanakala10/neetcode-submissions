class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            themap = {}
            for i in nums:
                if i in themap:
                    themap[i] += 1
                else:
                    themap[i] = 1

            print(themap.get)
            result = sorted(themap, key = lambda t: themap[t], reverse =True)
            return result[:k]