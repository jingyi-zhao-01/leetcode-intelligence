# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: unique-paths
# source_path: LeetCode-Solutions-master/Python/unique-paths.py
# solution_class: Solution
# submission_id: 10918d488a680d2446ab86a848e32f138602c124
# seed: 3096829717

# Time:  O(m + n)
# Space: O(1)

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        def nCr(n, r):  # Time: O(n), Space: O(1)
            if n-r < r:
                r = n-r
            c = 1
            for k in xrange(1, r+1):
                c *= n-k+1
                c //= k
            return c

        return nCr((m-1)+(n-1), n-1)