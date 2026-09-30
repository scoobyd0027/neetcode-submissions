class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i, p in enumerate(points):
            x, y = p
            distance = math.sqrt(x * x + y * y)
            heapq.heappush(heap, (-distance, i))

            if len(heap) > k:
                heapq.heappop(heap)
        
        return [points[i] for _, i in heap]
