class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        low = float('inf')
        while left <= right:
            if nums[left] < nums[right]:
                low = min(low, nums[left])
            mid = (left + right) // 2
            low = min(low, nums[mid])
            if nums[mid] < nums[left]:
                right = mid - 1
            else:
                left = mid + 1
        return low
