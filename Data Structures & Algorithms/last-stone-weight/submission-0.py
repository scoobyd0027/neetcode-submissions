class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            s1, s2 = heapq.heappop(heap), heapq.heappop(heap)
            s3 = s2 - s1
            if s3 > 0:
                heapq.heappush(heap, -s3)
        
        return -heap[0] if heap else 0
