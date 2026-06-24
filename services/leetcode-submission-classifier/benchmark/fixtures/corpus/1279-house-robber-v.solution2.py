# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: house-robber-v
# source_path: LeetCode-Solutions-master/Python/house-robber-v.py
# solution_class: Solution2
# submission_id: 53458733df922e90e6ddedb400fff57e331652a1
# seed: 3454189404

# Time:  O(n)
# Space: O(1)

# dp

class Solution2(object):
    def rob(self, nums, colors):
        """
        :type nums: List[int]
        :type colors: List[int]
        :rtype: int
        """
        dp = [0]*2
        for i in xrange(len(nums)):
            dp[0], dp[1] = max(dp[0], dp[1]), (dp[0] if i-1 >= 0 and colors[i-1] == colors[i] else max(dp[0], dp[1]))+nums[i]
        return max(dp[0], dp[1])