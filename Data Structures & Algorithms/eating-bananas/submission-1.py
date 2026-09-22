class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_finish(k):
            total = h
            for p in piles:
                hours = math.ceil(p / k)
                total -= hours
                if total < 0:
                    return False
            return True
        

        l, r, m = 1, max(piles), 0
        finished = False
        while l < r:
            m = l + (r - l) // 2
            if can_finish(m):
                finished = True
                r = m
            else:
                l = m + 1
        return r
