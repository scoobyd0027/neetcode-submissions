class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        if sum(gas) < sum(cost):
            return -1

        res = 0
        total = 0
        for i in range(n * 2):
            total += gas[i % n] - cost[i % n]

            if total < 0:
                total = 0
                res = i + 1
                
        return res
