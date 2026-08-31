from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxf, res = 0, 0
        i = 0
        reps = 0
        freq = Counter()
        for j in range(len(s)):
            freq[s[j]] += 1
            maxf = max(maxf, freq[s[j]])
            
            while (j - i + 1) - maxf > k:
                freq[s[i]] -= 1
                i += 1
            
            res = max(res, j - i + 1)
            j += 1

        return res
