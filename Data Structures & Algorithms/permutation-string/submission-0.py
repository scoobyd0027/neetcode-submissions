from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts_s1 = Counter(s1)
        
        s1_len = len(s1)
        counts_s2 = Counter()
        i = 0
        for j in range(len(s2)):
            counts_s2[s2[j]] += 1
            while i <= j and counts_s2[s2[j]] > counts_s1[s2[j]]:
                counts_s2[s2[i]] -= 1
                i += 1
            
            if (j - i + 1) == s1_len:
                return True
        
        return False

