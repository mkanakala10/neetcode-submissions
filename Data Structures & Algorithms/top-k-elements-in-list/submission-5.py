class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums): 
            return nums
        
        hashmap = Counter(nums)
        return heapq.nlargest(k, hashmap.keys(), key = hashmap.get)