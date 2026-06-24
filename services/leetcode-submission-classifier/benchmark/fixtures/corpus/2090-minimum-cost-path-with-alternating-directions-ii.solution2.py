# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-cost-path-with-alternating-directions-ii
# source_path: LeetCode-Solutions-master/Python/minimum-cost-path-with-alternating-directions-ii.py
# solution_class: Solution2
# submission_id: 357ba822fbce5f29f4b969b2750af0d842ec3ed7
# seed: 1737098426

# Time:  O(m * n)
# Space: O(1)

# dp

class Solution2(object):
    def minCost(self, m, n, waitCost):
        """
        :type m: int
        :type n: int
        :type waitCost: List[List[int]]
        :rtype: int
        """
        waitCost[0][0] = waitCost[m-1][n-1] = 0
        dp = [0]*n
        for i in xrange(m):
            for j in xrange(n):
                prev = 0 if (i, j) == (0, 0) else float("inf")
                if i-1 >= 0:
                    prev = min(prev, dp[j])
                if j-1 >= 0:
                    prev = min(prev, dp[j-1])
                dp[j] = prev+waitCost[i][j]+(i+1)*(j+1)
        return dp[n-1]