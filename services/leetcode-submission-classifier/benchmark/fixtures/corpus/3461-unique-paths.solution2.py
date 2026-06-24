# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: unique-paths
# source_path: LeetCode-Solutions-master/Python/unique-paths.py
# solution_class: Solution2
# submission_id: c9bb6efbd4c86afd65183dbc9924b457f7820b34
# seed: 3942717744

# Time:  O(m + n)
# Space: O(1)

class Solution2(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m < n:
            m, n  = n, m

        dp = [1]*n
        for i in xrange(1, m):
            for j in xrange(1, n):
                dp[j] += dp[j-1]
        return dp[n-1]