class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n, m = len(heights), len(heights[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        pac, atl = set(), set()

        def is_valid(i, j, vis, h):
            return 0 <= i < n and 0 <= j < m \
            and (i, j) not in vis and heights[i][j] >= h

        def dfs(i, j, vis, h):
            if not is_valid(i, j, vis, h):
                return
            
            vis.add((i, j))
            h = heights[i][j]
            for x, y in directions:
                ni, nj = i + x, j + y
                dfs(ni, nj, vis, h)
        
        for c in range(m):
            dfs(0, c, pac, heights[0][c])
            dfs(n - 1, c, atl, heights[n - 1][c])
        
        for r in range(n):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, m - 1, atl, heights[r][m - 1])
        
        res = []
        for i in range(n):
            for j in range(m):
                if (i, j) in pac and (i, j) in atl:
                    res.append((i, j))
        
        return res

