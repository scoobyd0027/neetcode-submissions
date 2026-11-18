class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp = [sys.maxsize] * (len(cost) + 1)
        # dp[0] = 0
        # dp[1] = 0

        cur, prev = 0, 0
        for i in range(2, len(cost) + 1):
            # dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])     
            new = min(cur + cost[i - 1], prev + cost[i - 2])
            cur, prev = new, cur
        return cur