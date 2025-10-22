# House Robber II - Wrong Solution

class Solution:
    def rob(self, nums) -> int:
        if len(nums) == 1:
            return nums[0]
        
        prev2 = prev1 = 0
        for num in nums:
            curr = max(prev1, prev2 + num)
            prev2 = prev1
            prev1 = curr
        return prev1