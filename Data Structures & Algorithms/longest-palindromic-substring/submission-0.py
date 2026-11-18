from functools import lru_cache
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i, j = i - 1, j + 1
            return i + 1, j - 1
        
        mi, mj = 0, 0
        for i in range(len(s)):
            for x, y in [(i, i), (i, i + 1)]:
                a, b = expand(x, y)
                if (b - a) > (mj - mi):
                    mi, mj = a, b
        return s[mi: mj + 1]

'''
ababd
aba
 bab
  a
   b
    d
'''