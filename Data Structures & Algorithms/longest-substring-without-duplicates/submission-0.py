from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counts = Counter()
        i, j = 0, 0
        longest = 0
        while j < len(s):
            counts[s[j]] += 1
            while i < j and counts[s[j]] > 1:
                counts[s[i]] -= 1
                i += 1
            
            longest = max(longest, j - i + 1)
            j += 1

        return longest