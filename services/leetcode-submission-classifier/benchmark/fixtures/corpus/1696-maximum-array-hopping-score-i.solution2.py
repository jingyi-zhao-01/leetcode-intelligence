# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-array-hopping-score-i
# source_path: LeetCode-Solutions-master/Python/maximum-array-hopping-score-i.py
# solution_class: Solution2
# submission_id: 6a95b2876e3ac092281e6c55bab5d335036685b8
# seed: 1142929330

# Time:  O(n)
# Space: O(1)

# prefix sum, greedy

class Solution2(object):
    def maxScore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0]*len(nums)
        for i in xrange(1, len(nums)):
            for j in xrange(i):
                dp[i] = max(dp[i], dp[j]+(i-j)*nums[i])
        return dp[-1]