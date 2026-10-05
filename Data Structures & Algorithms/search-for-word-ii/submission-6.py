from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None
        self.endWord = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        n, m = len(board), len(board[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        root = TrieNode()
        node = root
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word
            node.endWord = True
    
        res = []
        def dfs(i, j, node):
            if not 0 <= i < n or not 0 <= j < m:
                return                

            if board[i][j] in node.children:
                char = board[i][j]
                board[i][j] = '#'
                child = node.children[char]
                if child.endWord:
                    child.endWord = False
                    res.append(child.word)

                for x, y in directions:
                    dfs(i + x, j + y, child)
                
                board[i][j] = char
        

        for i in range(n):
            for j in range(m):
                dfs(i, j, root)
        
        return res


        

