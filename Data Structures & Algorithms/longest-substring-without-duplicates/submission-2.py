from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        i, j = 0, 0
        longest = 0
        while j < len(s):
            if s[j] in map:
                i = max(map[s[j]] + 1, i)

            map[s[j]] = j
            longest = max(longest, j - i + 1)
            j += 1

        return longest