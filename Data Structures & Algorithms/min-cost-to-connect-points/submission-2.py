class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def mandistance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        
        q = [(0, 0)]
        total = 0
        seen = set()
        while q:
            dist, j = heapq.heappop(q) 
            if j in seen: continue
            seen.add(j)
            total += dist
            for i in range(len(points)):
                if i in seen: continue
                md = mandistance(points[j], points[i])
                heapq.heappush(q, (md, i))

        return total