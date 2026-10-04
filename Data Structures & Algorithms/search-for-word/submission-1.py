class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def backtrack(r, c, i, seen):
            nonlocal board, word, n, m
            if i == len(word): return True
            if not 0 <= r < n or not 0 <= c < m or (r, c) in seen:
                return False
            
            if board[r][c] == word[i]:
                seen.add((r, c))
                for x, y in directions:
                    if backtrack(r + x, c + y, i + 1, seen):
                        return True
                seen.remove((r, c))
            return False
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if backtrack(i, j, 0, set()):
                        return True
        
        return False
