class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        if n == 0: return 0

        def is_valid(i, j):
            return 0 <= i < n and 0 <= j < m and grid[i][j] != -1

        q = [(grid[0][0], (0, 0))]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while q:
            dist, (i, j) = heapq.heappop(q)
            if grid[i][j] == -1: continue
            if (i, j) == (n - 1, m - 1):
                return dist
            
            grid[i][j] = -1
            for x, y in directions:
                ni, nj = i + x, j + y
                if is_valid(ni, nj):
                    heapq.heappush(q, (max(dist, grid[ni][nj]), (ni, nj)))
        
        return -1  
