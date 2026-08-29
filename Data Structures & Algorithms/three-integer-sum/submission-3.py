class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        nums.sort()
        i = 0
        while i < n:
            seen = set()
            j = i + 1
            while j < n:
                target = 0 - nums[i] - nums[j]
                if target in seen:
                    res.append([nums[i], nums[j], target])
                    while j + 1 < n and nums[j] == nums[j + 1]:
                        j += 1

                seen.add(nums[j])
                j += 1

            
            i += 1
            while i < n and nums[i] == nums[i - 1]:
                i += 1
        
        return res

