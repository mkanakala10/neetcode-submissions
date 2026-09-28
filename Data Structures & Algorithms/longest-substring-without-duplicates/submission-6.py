class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        left = 0
        tempset = set()

        for right in range(len(s)):
            while s[right] in tempset:
                tempset.remove(s[left])
                left += 1
            tempset.add(s[right])

            longest = max(longest, right - left + 1)

        return longest