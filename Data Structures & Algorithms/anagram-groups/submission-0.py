class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        themap = defaultdict(list)
        for string in strs:
            count = [0] * 26
            for char in string:
                count[ord(char) - ord("a")] += 1
            themap[tuple(count)].append(string)
        return themap.values()
            