from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        temp = Counter(t)
        min_len = float('inf')
        res = ""
        my_dict = defaultdict(int)
        left = count = 0

        for right in range(len(s)):
            my_dict[s[right]] += 1
            
            if s[right] in temp and my_dict[s[right]] == temp[s[right]]: 
                count += 1
            if count == len(temp):
                while count == len(temp):
                    if (right - left + 1) < min_len:
                        res = s[left : right + 1]
                        min_len = len(res)
                    my_dict[s[left]] -= 1
                    if s[left] in temp and my_dict[s[left]] < temp[s[left]]:
                        my_dict[s[left]] += 1
                        break
                    left += 1
        return res