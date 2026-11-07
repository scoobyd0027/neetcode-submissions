class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        q = []
        intervals.sort()

        qs = sorted([(queries[i], i) for i in range(len(queries))])
        res = [-1] * len(queries)        
        j = 0
        for i in range(len(qs)):
            while j < len(intervals) and intervals[j][0] <= qs[i][0]:
                s, e = intervals[j]
                heapq.heappush(q, (e - s + 1, e))
                j += 1
            
            while q and q[0][1] < qs[i][0]:
                heapq.heappop(q)
            
            if q:
                res[qs[i][1]] = q[0][0]
        return res
