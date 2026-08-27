from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = Counter(s)
        for ch in t:
            if ch not in counts:
                return False
            
            counts[ch] -= 1
            if counts[ch] < 0:
                return False
        
        return len(s) == len(t)