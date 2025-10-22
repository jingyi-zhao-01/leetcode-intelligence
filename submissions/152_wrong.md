# Maximum Product Subarray - Wrong Solution

class Solution:
    def maxProduct(self, nums):
        if not nums:
            return 0
        
        max_prod = result = nums[0]
        
        for i in range(1, len(nums)):
            max_prod = max(nums[i], max_prod * nums[i])
            result = max(result, max_prod)
        
        return result