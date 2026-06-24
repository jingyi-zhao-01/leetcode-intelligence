# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: house-robber-v
# source_path: LeetCode-Solutions-master/Python/house-robber-v.py
# solution_class: Solution
# submission_id: bcd4dfbfa8dc1c8f24898f65743b463755a3cdab
# seed: 3449670894

# Time:  O(n)
# Space: O(1)

# dp

class Solution(object):
    def rob(self, nums, colors):
        """
        :type nums: List[int]
        :type colors: List[int]
        :rtype: int
        """
        dp = [0]*2
        for i in xrange(len(nums)):
            dp[i%2] = max(dp[(i-2)%2]+nums[i], dp[(i-1)%2]) if i-1 >= 0 and colors[i-1] == colors[i] else dp[(i-1)%2]+nums[i]
        return dp[(len(nums)-1)%2]