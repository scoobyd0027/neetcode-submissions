from functools import lru_cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)
        def dfs(total):
            if total == amount: return 0

            min_coins = sys.maxsize
            for c in coins:
                if total + c <= amount:
                    min_coins = min(min_coins, dfs(total + c) + 1)
            return min_coins

        res = dfs(0)
        return res if res != sys.maxsize else -1
