class MedianFinder:

    def __init__(self):
        self.minHeap, self.maxHeap = [], [] 
        self.size = 0
        # maxHeap ->  minHeap 

    def addNum(self, num: int) -> None:
        if self.maxHeap and num < -self.maxHeap[0]:
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)
            
        while len(self.maxHeap) > len(self.minHeap):
            num = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, num)
        
        while len(self.minHeap) > (len(self.maxHeap) + 1):
            num = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -num)

        self.size += 1

    def findMedian(self) -> float:
        if self.size % 2 == 0:
            maxNum = -self.maxHeap[0]
            minNum = self.minHeap[0]
            return (maxNum + minNum) / 2
        return self.minHeap[0]
        