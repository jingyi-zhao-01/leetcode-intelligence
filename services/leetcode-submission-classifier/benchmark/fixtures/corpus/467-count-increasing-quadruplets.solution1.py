# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-increasing-quadruplets
# source_path: LeetCode-Solutions-master/Python/count-increasing-quadruplets.py
# solution_class: Solution
# submission_id: 71cb60b820e9253fc2d45fdac715a53388e2fff8
# seed: 4119663058

# Time:  O(n^2)
# Space: O(n)

# dp

class Solution(object):
    def countQuadruplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0]*len(nums)  # dp[j] at l: # of tuple (i, j, k) s.t. i < j < k < l and nums[i] < nums[k] < nums[j]
        result = 0
        for l in xrange(len(nums)):
            cnt = 0
            for j in xrange(l):
                if nums[j] < nums[l]:
                    cnt += 1
                    result += dp[j]
                elif nums[j] > nums[l]:
                    dp[j] += cnt
        return result