from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        counts = Counter(tasks)

        for t, count in counts.items():
            heap.append(-count)
        
        heapq.heapify(heap)

        cycles = 0
        q = deque()
        while heap or q:
            cycles += 1

            if not heap:
                cycles = q[0][1]
            else:
                count = heapq.heappop(heap)
                count += 1
                if count < 0:
                    q.append([count, cycles + n])
            
            if q and q[0][1] == cycles:
                heapq.heappush(heap, q.popleft()[0])
        return cycles

'''
A -> B -> C -> D -> E -> F -> G -> A
'''