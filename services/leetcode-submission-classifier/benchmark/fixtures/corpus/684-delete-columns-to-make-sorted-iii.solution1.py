# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: delete-columns-to-make-sorted-iii
# source_path: LeetCode-Solutions-master/Python/delete-columns-to-make-sorted-iii.py
# solution_class: Solution
# submission_id: 61b9f6b843db0d33a3ae57ff5be33d1ec6c687bd
# seed: 1662043850

# Time:  O(n * l^2)
# Space: O(l)

class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        dp = [1] * len(A[0])
        for j in xrange(1, len(A[0])):
            for i in xrange(j):
                if all(A[k][i] <= A[k][j] for k in xrange(len(A))):
                    dp[j] = max(dp[j], dp[i]+1)
        return len(A[0]) - max(dp)