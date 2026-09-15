class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = (s.replace(" ", "")).lower()
        s = re.sub('[^0-9a-zA-Z]+', '', s)
        print(s)
        if len(s) % 2 == 0:
            left = int(len(s) / 2) - 1
            right = int(len(s) / 2)
        else:
            left = int(len(s) / 2) - 1 
            right = int(len(s) / 2) + 1
        
        for i in range(int(len(s) / 2)):
            print(s[left - i])
            print(s[right + i])
            if s[left - i] != s[right + i]:
                return False
        return True