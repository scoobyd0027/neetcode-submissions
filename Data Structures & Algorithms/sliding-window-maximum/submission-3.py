class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = []
        res = []
        j = 0
        for i in range(len(nums)):
            while d and nums[d[-1]] < nums[i]:
                d.pop()

            d.append(i)
            if j > d[0]:
                d.pop(0)

            if i >= k - 1:
                res.append(nums[d[0]])
                j += 1
        
        return res
            
