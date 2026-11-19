class Solution:
    def numDecodings(self, s: str) -> int:
        prev = int(s[0])
        if prev == 0: return 0

        dp = [0] * len(s)
        dp[0] = 1
        for i in range(1, len(s)):
            cur = int(s[i])

            if cur != 0:
                dp[i] = dp[i - 1]

            comb = prev * 10 + cur
            if 10 <= comb <= 26:
                dp[i] += dp[i - 2] if i >= 2 else 1
            prev = cur
        
        return dp[-1]

