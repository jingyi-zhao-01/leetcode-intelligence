# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-increment-operations-to-make-array-beautiful
# source_path: LeetCode-Solutions-master/Python/minimum-increment-operations-to-make-array-beautiful.py
# solution_class: Solution
# submission_id: 3614a3c26cc5041caded70cdf469ac9846b10767
# seed: 3527064709

# Time:  O(n)
# Space: O(1)

# dp

class Solution(object):
    def minIncrementOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        W = 3
        dp = [0]*W
        for i, x in enumerate(nums):
            dp[i%W] = min(dp[j%W] for j in xrange(i-W, i))+max(k-x, 0)
        return min(dp)