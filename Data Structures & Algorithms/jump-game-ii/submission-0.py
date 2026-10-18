class Solution:
    def jump(self, nums: List[int]) -> int:
        j = len(nums) - 1
        dp = [sys.maxsize] * len(nums)
        dp[-1] = 0
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= i + 1:
                max_idx = min(i + nums[i], j)
                dp[i] = min(dp[i + 1], dp[max_idx]) + 1
        return dp[0]
