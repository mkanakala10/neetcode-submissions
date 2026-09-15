class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs: 
            string += (str(len(s)) + "%" + s)
        return string
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            y = i
            length = ""
            for x in s[i:]:
                if x == "%":
                    break
                length += x
            j = i + 1 + len(length)
            string = ""
            total = int(length) + j
            while j < total:
                string += s[j]
                j += 1
            result.append(string)
            i = total
        return result