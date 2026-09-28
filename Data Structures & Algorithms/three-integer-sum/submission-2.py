class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen = set()
        nums.sort()

        for i in range(len(nums) - 1):
            l = i + 1
            r = len(nums) - 1
            while r > l:
                if (nums[i] + nums[l] + nums[r]) > 0:
                    r -= 1
                elif (nums[i] + nums[l] + nums[r]) < 0:
                    l += 1
                else:
                    if (nums[i], nums[l], nums[r]) not in seen:
                        res.append([nums[i], nums[l], nums[r]])
                        seen.add((nums[i], nums[l], nums[r]))
                    r -= 1
                    l += 1
        return res
# -4, -1, -1, 0, 1, 2