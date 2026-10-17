class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = nums[0]
        max_sum = total
        for i in range(1, len(nums)):
            total = max(total + nums[i], nums[i])
            max_sum = max(max_sum, total)
        return max_sum