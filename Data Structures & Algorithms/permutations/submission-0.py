class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(cur, chosen):
            nonlocal res
            if len(cur) == len(nums):
                res.append(cur.copy())
                return

            for i in range(len(nums)):
                if not chosen[i]:
                    cur.append(nums[i])
                    chosen[i] = True
                    backtrack(cur, chosen)
                    chosen[i] = False
                    cur.pop()
        
        backtrack([], [False] * len(nums))
        return res
                