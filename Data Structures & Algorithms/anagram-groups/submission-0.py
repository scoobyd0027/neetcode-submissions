class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for str in strs:
            universal = "".join(sorted(str))
            if universal not in anagrams:
                anagrams[universal] = []
            anagrams[universal].append(str)
        return list(anagrams.values())
