class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets = [[]]
        for i, num in enumerate(nums):
            idx = prev_idx if i >= 1 and num == nums[i - 1] else 0
            prev_idx = len(subsets)
            for j in range(idx, prev_idx):
                c = subsets[j].copy()
                c.append(num)
                subsets.append(c)
        return subsets
