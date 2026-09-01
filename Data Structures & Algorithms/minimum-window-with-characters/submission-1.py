class Solution:
    def minWindow(self, s: str, t: str) -> str:
        i, j = 0, 0
        si, sj = 0, sys.maxsize
        t_counts = Counter(t)
        s_counts = Counter()
        matches = 0
        for j in range(len(s)):
            s_counts[s[j]] += 1
            if s[j] in t_counts and t_counts[s[j]] == s_counts[s[j]]:
                matches += 1
            
            while matches == len(t_counts):
                if sj - si > j - i:
                    si, sj = i, j
                
                s_counts[s[i]] -= 1
                if s[i] in t_counts and t_counts[s[i]] > s_counts[s[i]]:
                    matches -= 1
                i += 1
        
        return s[si: sj + 1] if sj != sys.maxsize else ""