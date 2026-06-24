# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-falling-path-sum
# source_path: LeetCode-Solutions-master/Python/minimum-falling-path-sum.py
# solution_class: Solution
# submission_id: f43f59d5b56ff370dc5fe19690a27ea142cc1726
# seed: 2037332124

# Time:  O(n^2)
# Space: O(1)

class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        for i in xrange(1, len(A)):
            for j in xrange(len(A[i])):
                A[i][j] += min(A[i-1][max(j-1, 0):j+2])
        return min(A[-1])