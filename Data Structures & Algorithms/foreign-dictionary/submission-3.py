from collections import defaultdict, Counter

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        depends = {c: set() for w in words for c in w}
        indegrees = {c: 0 for c in depends}

        def buildGraph(word1, word2):
            i, j = 0, 0
            n, m = len(word1), len(word2)
            while i < n and j < m and word1[i] == word2[j]:
                i, j = i + 1, j + 1
            
            if i < n and j == m:
                return False
            
            while i < n and j < m:
                if word1[i] != word2[j]:
                    if word2[j] not in depends[word1[i]]:
                        indegrees[word2[j]] += 1
                        depends[word1[i]].add(word2[j])
                    break
                i, j = i + 1, j + 1
            return True

        for i in range(len(words) - 1):
            if not buildGraph(words[i], words[i + 1]):
                return ""

        q = deque()
        for ch in depends:
            if indegrees[ch] == 0:
                q.append(ch)
        
        res = []
        while q:
            ch = q.popleft()
            res.append(ch)

            for next in depends[ch]:
                indegrees[next] -= 1
                if indegrees[next] == 0:
                    q.append(next)
        
        return "".join(res) if len(res) == len(indegrees) else ""
