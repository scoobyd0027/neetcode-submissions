class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        n, m = len(grid), len(grid[0])
        def traverse(i, j):
            if not (0 <= i < n and 0 <= j < m) or grid[i][j] != '1':
                return
            
            grid[i][j] = '#'
            for x, y in directions:
                traverse(i + x, j + y)
            
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    traverse(i, j)
                    count += 1
        
        return count
