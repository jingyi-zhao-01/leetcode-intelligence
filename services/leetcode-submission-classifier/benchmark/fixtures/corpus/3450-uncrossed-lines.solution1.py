# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: uncrossed-lines
# source_path: LeetCode-Solutions-master/Python/uncrossed-lines.py
# solution_class: Solution
# submission_id: bd92019a76e3e731d96a79a11d087aaf7c9cdfe1
# seed: 1266104292

# Time:  O(m * n)
# Space: O(min(m, n))

class Solution(object):
    def maxUncrossedLines(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        if len(A) < len(B):
            return self.maxUncrossedLines(B, A)

        dp = [[0 for _ in xrange(len(B)+1)] for _ in xrange(2)]
        for i in xrange(len(A)):
            for j in xrange(len(B)):
                dp[(i+1)%2][j+1] = max(dp[i%2][j] + int(A[i] == B[j]),
                                       dp[i%2][j+1],
                                       dp[(i+1)%2][j])
        return dp[len(A)%2][len(B)]