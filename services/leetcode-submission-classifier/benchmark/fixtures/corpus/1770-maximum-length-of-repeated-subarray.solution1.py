# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-length-of-repeated-subarray
# source_path: LeetCode-Solutions-master/Python/maximum-length-of-repeated-subarray.py
# solution_class: Solution
# submission_id: 3b71c682e213f83790aef8a00139cba3d8d86664
# seed: 3851613686

# Time:  O(m * n)
# Space: O(min(m, n))

import collections

class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        if len(A) < len(B): return self.findLength(B, A)
        result = 0
        dp = [[0] * (len(B)+1) for _ in xrange(2)]
        for i in xrange(len(A)):
            for j in xrange(len(B)):
                if A[i] == B[j]:
                    dp[(i+1)%2][j+1] = dp[i%2][j]+1
                else:
                    dp[(i+1)%2][j+1] = 0
            result = max(result, max(dp[(i+1)%2]))
        return result