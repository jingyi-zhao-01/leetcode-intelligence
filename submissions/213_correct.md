# House Robber II - Correct Solution

class Solution:
    def rob(self, nums) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        
        def rob_linear(houses):
            prev2 = prev1 = 0
            for num in houses:
                curr = max(prev1, prev2 + num)
                prev2 = prev1
                prev1 = curr
            return prev1
        
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))