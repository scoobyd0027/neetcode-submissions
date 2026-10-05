class UF:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)
    
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        
        if self.size[pu] >= self.size[pv]:
            self.size[pu] += self.size[pv]
            self.parent[pv] = pu
        else:
            self.size[pv] += self.size[pu]
            self.parent[pu] = pv
        
        return True

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        uf = UF(n * m)
        def index(r, c):
            return r * m + c

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        islands = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    islands += 1
                    for x, y in directions:
                        nr, nc = i + x, j + y
                        if not (0 <= nr < n and 0 <= nc < m) or grid[nr][nc] != '1':
                            continue
                        
                        if uf.union(index(i, j), index(nr, nc)):
                            islands -= 1
            
        return islands
                

        