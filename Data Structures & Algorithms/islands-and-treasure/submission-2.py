class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n, m = len(grid), len(grid[0])
        visit = set()

        def is_valid(i, j):
            return 0 <= i < n and 0 <= j < m and (i, j) not in visit

        q = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    visit.add((i, j))
                    q.append((0, i, j))
        
        notset = 2147483647
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        while q:
            dis, i, j = q.popleft()
            dis += 1
            for x, y in directions:
                ni, nj = i + x, j + y
                if is_valid(ni, nj) and grid[ni][nj] > dis:
                    grid[ni][nj] = dis
                    visit.add((ni, nj))
                    q.append((dis, ni, nj))
            
        return


        
