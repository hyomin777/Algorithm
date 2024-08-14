class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = min_product = result = nums[0]

        for i in range(1, len(nums)):
            temp_max = max_product

            max_product = max(nums[i], nums[i] * temp_max, nums[i] * min_product)
            min_product = min(nums[i], nums[i] * temp_max, nums[i] * min_product)

            result = max(result, max_product)

        return result