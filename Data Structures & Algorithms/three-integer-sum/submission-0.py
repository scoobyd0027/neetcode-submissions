class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = set()
        for i in range(n):
            seen = set()
            for j in range(i + 1, n):
                target = 0 - nums[i] - nums[j]
                if target in seen:
                    res.add(tuple(sorted([nums[i], nums[j], target])))
                seen.add(nums[j])
        return list([list(t) for t in res])
