class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        left = 0
        tempset = set()

        for right in range(len(s)):
            while s[right] in tempset:
                # Remove the leftmost character and move the window forward
                tempset.remove(s[left])
                left += 1
            
            # Add the current character to the set
            tempset.add(s[right])

            # Calculate the longest length
            longest = max(longest, right - left + 1)

        return longest