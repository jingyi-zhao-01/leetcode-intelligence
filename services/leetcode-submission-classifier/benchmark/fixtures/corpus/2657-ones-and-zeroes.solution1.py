# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: ones-and-zeroes
# source_path: LeetCode-Solutions-master/Python/ones-and-zeroes.py
# solution_class: Solution
# submission_id: e63bf6e552fe8c08654dc3d8b7f152a1c9805a1e
# seed: 2550161786

# Time:  O(s * m * n), s is the size of the array.
# Space: O(m * n)

class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for _ in xrange(n+1)] for _ in xrange(m+1)]
        for s in strs:
            zero_count, one_count = 0, 0
            for c in s:
                if c == '0':
                    zero_count += 1
                elif c == '1':
                    one_count += 1

            for i in reversed(xrange(zero_count, m+1)):
            	for j in reversed(xrange(one_count, n+1)):
                    dp[i][j] = max(dp[i][j], dp[i-zero_count][j-one_count]+1)
        return dp[m][n]