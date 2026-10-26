class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counts = Counter()
        totals = Counter(s)
        i, j = 0, 0
        res = []
        matches = 0
        while j < len(s):
            counts[s[j]] += 1

            if counts[s[j]] == totals[s[j]]:
                matches += counts[s[j]]
            
                if matches == j - i + 1:
                    res.append(matches)
                    matches = 0
                    counts = Counter()
                    i = j + 1
            j += 1
        
        return res
