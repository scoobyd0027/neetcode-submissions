from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        bucket = [[] for i in range(len(nums) + 1)]

        for num, count in counts.items():
            bucket[count].append(num)
        
        res = []
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                res.append(num)

                if len(res) == k:
                    return res
        
        return res
