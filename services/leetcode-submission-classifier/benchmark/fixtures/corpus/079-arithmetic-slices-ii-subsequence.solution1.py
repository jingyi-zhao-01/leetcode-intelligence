# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: arithmetic-slices-ii-subsequence
# source_path: LeetCode-Solutions-master/Python/arithmetic-slices-ii-subsequence.py
# solution_class: Solution
# submission_id: 075e6fdb29d9e0ae5c5c80e65e17430afc8287fe
# seed: 2302215882

# Time:  O(n^2)
# Space: O(n * d)

import collections

class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        result = 0
        dp = [collections.defaultdict(int) for i in xrange(len(A))]
        for i in xrange(1, len(A)):
            for j in xrange(i):
                diff = A[i]-A[j]
                dp[i][diff] += 1
                if diff in dp[j]:
                    dp[i][diff] += dp[j][diff]
                    result += dp[j][diff]
        return result