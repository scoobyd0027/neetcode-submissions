class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        n, m = len(grid), len(grid[0])
        def traverse(i, j):
            if not (0 <= i < n and 0 <= j < m) or grid[i][j] != 1:
                return 0
            
            grid[i][j] = 0
            total = 1
            for x, y in directions:
                total += traverse(i + x, j + y)
            return total
            
        maxArea = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    area = traverse(i, j)
                    maxArea = max(maxArea, area)
        
        return maxArea