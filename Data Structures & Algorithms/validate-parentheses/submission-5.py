class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        maps = {")": "(", "}": "{", "]": "["}
        stack = []
        for i in s:
            if i not in maps:
                stack.append(i)
                print(stack)
                continue
            print(i)
            if i not in maps:
                return False
            if not stack:
                return False
            obj = stack.pop()
            if maps[i] != obj:
                return False
            
        return not stack
            
