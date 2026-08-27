from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        counts = Counter(nums)

        for num, count in counts.items():
            heapq.heappush(heap, (count, num))
                        
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [v for c, v in heap]
