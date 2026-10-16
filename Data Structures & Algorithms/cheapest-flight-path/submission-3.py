class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for from_i, to_i, price_i in flights:
            adj[from_i].append((price_i, to_i))
        
        q = [(0, -1, src)]
        dist = [[sys.maxsize] * (k + 5) for _ in range(n)]
        dist[src][0] = 0
        while q:
            price, con, air = heapq.heappop(q)
            if air == dst:
                return price

            if con == k or dist[air][con + 1] < price:
                continue
            
            for cost, next in adj[air]:
                nextCst = price + cost
                nextStops = con + 1
                if dist[next][nextStops + 1] > nextCst:
                    dist[next][nextStops + 1] = nextCst
                    heapq.heappush(q, (price + cost, con + 1, next))
    
        return -1
