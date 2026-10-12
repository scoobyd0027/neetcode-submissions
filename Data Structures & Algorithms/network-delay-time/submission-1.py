from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, t in times:
            graph[u].append((t, v))
        
        q = deque([(0, k)])
        travelTimes = [sys.maxsize] * n
        travelTimes[k - 1] = 0
        while q:
            t, n = q.popleft()

            for time, neig in graph[n]:
                if travelTimes[neig - 1] > time + t:
                    q.append((t + time, neig))
                    travelTimes[neig - 1] = time + t
        
        max_t = max(travelTimes) 
        return max_t if max_t != sys.maxsize else -1
