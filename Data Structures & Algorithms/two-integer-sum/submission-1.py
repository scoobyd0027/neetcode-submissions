class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            half = target - num
            if half in seen:
                return [seen[half], i]
            seen[num] = i
        return []
