# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-maximum-length-of-valid-subsequence-i
# source_path: LeetCode-Solutions-master/Python/find-the-maximum-length-of-valid-subsequence-i.py
# solution_class: Solution
# submission_id: ec21c3f7a2297723d90d6f126d482884a3febff7
# seed: 1373076427

# Time:  O(n)
# Space: O(1)

# dp

class Solution(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        k = 2
        result = 0
        for i in xrange(k):
            dp = [0]*k
            for x in nums:
                dp[x%k] = dp[(i-x)%k]+1
            result = max(result, max(dp))
        return result