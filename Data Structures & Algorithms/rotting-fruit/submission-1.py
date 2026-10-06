class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        q = deque()
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i, j))
        
        mins = 0
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def is_valid(i, j):
            return 0 <= i < n and 0 <= j < m and grid[i][j] == 1

        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                for x, y in directions:
                    ni, nj = i + x, j + y
                    if is_valid(ni, nj):
                        grid[ni][nj] = 2
                        fresh -= 1
                        q.append((ni, nj))
            mins += 1
        return max(mins - 1, 0) if fresh == 0 else -1

