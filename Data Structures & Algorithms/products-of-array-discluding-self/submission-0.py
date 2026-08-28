class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        left_products = [1]
        for num in nums:
            product *= num
            left_products.append(product)
        
        product = 1
        res = []
        for i in range(len(nums) - 1, -1, -1):
            total = left_products[i] * product
            product *= nums[i]
            res.append(total)

        return res[::-1]
