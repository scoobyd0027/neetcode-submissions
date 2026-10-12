import heapq

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = deque([(1, beginWord)])
        wordSet = set(wordList)
        vis = set(beginWord)
        while q:
            dist, word = q.popleft()
            if word == endWord:
                return dist
            
            for i in range(len(word)):
                for j in range(26):
                    c = chr(ord('a') + j)
                    if c == word[i]: continue
                    newWord = word[:i] + c + word[i + 1:]
                    if newWord in wordSet and newWord not in vis:
                        vis.add(newWord)
                        q.append((dist + 1, newWord))
        return 0

