class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        highest = [0] * len(height)
        high = 0
        for j in range(len(height) - 1, -1, -1):
            high = max(high, height[j])
            highest[j] = high

        high = 0
        for i in range(len(height)):
            total += max(min(high, highest[i]) - height[i], 0)
            high = max(high, height[i])
        
        return total
