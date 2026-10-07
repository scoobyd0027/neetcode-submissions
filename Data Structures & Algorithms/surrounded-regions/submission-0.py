class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n, m = len(board), len(board[0])
        edges = [[False] * m for _ in range(n)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def is_valid(i, j):
            return 0 <= i < n and 0 <= j < m and edges[i][j] is False and board[i][j] == 'O'

        def traverse(i, j):
            if not is_valid(i, j): return
            edges[i][j] = True

            for x, y in directions:
                ni, nj = i + x, j + y
                traverse(ni, nj)

        for i in range(n):
            traverse(i, 0)
            traverse(i, m - 1)

        for j in range(m):
            traverse(0, j)
            traverse(n - 1, j)

        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O' and edges[i][j] is False:
                    board[i][j] = 'X'