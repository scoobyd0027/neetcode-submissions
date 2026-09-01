class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        res = []
        for i, num in enumerate(nums):
            heapq.heappush(heap, (-num, i))

            while heap and heap[0][1] <= i - k:
                heapq.heappop(heap)
            
            if i >= k - 1:
                res.append(-heap[0][0])
        
        return res

