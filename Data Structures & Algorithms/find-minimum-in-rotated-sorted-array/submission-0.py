class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[l] <= nums[r]:
                return nums[l]
            else:
                if nums[m] >= nums[l]:
                    l = m + 1
                else:
                    r = m
        return nums[r]
