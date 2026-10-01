class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(i, cur, total):
            nonlocal res, nums, target
            if total > target: return

            if i >= len(nums): 
                if total == target:
                    res.append(cur.copy())
                return

            cur.append(nums[i])
            backtrack(i, cur, total + nums[i])
            cur.remove(nums[i])

            backtrack(i + 1, cur, total)
        
        backtrack(0, [], 0)
        return res