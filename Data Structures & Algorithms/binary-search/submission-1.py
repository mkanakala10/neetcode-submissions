class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2
        while nums[mid] != target:
            if target == nums[left]:
                return left
            if target == nums[right]:
                return right
            if target > nums[mid]:
                left = mid 
            else:
                right = mid
            mid = (left + right) // 2

            if mid == left or mid == right:
                return -1
        return mid