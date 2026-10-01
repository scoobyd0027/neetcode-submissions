class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(i, cur):
            nonlocal res, nums
            if i >= len(nums): 
                res.append(cur.copy())
                return

            cur.append(nums[i])
            backtrack(i + 1, cur)
            cur.remove(nums[i])

            backtrack(i + 1, cur)
        
        backtrack(0, [])
        return res
