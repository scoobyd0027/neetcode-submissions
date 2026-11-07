class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * ( n + 1)
        for i in range(n + 1):
            dp[i] = dp[i >> 1] + (i & 1)
        return dp

'''
[0, 1, 1, 2, 1, 2, 2, 3, 2, 3, 3, 4, 3, 4, 4, 5]
0 -> 1 -> 10 -> 11 -> 100 -> 101 -> 110 -> 111 -> 1000 -> 1001 -> 1010 -> 1011 -> 1100 -> 1101 -> 1110 -> 1111
'''