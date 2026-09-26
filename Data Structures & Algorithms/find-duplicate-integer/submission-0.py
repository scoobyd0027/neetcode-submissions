class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        map = 0
        for num in nums:
            if map & (1 << num):
                return num

            map |= (1 << num)
        return -1 