# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-cost-path-with-alternating-directions-ii
# source_path: LeetCode-Solutions-master/Python/minimum-cost-path-with-alternating-directions-ii.py
# solution_class: Solution
# submission_id: 31e928e3b8fad6fd355767cf95c57b3a29132c0e
# seed: 3584777002

# Time:  O(m * n)
# Space: O(1)

# dp

class Solution(object):
    def minCost(self, m, n, waitCost):
        """
        :type m: int
        :type n: int
        :type waitCost: List[List[int]]
        :rtype: int
        """
        waitCost[0][0] = waitCost[m-1][n-1] = 0
        for i in xrange(m):
            for j in xrange(n):
                prev = 0 if (i, j) == (0, 0) else float("inf")
                if i-1 >= 0:
                    prev = min(prev, waitCost[i-1][j])
                if j-1 >= 0:
                    prev = min(prev, waitCost[i][j-1])
                waitCost[i][j] += prev+(i+1)*(j+1)
        return waitCost[m-1][n-1]