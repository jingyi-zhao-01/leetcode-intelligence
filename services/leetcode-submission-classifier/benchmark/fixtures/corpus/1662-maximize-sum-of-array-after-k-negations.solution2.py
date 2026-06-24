# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximize-sum-of-array-after-k-negations
# source_path: LeetCode-Solutions-master/Python/maximize-sum-of-array-after-k-negations.py
# solution_class: Solution2
# submission_id: 766c77b619494946de4e8a1b51b5a7a869f911c8
# seed: 2038360548

# Time:  O(n) ~ O(n^2), O(n) on average.
# Space: O(1)

import random


# quick select solution

class Solution2(object):
    def largestSumAfterKNegations(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A.sort()
        remain = K
        for i in xrange(K):
            if A[i] >= 0:
                break
            A[i] = -A[i]
            remain -= 1
        return sum(A) - (remain%2)*min(A)*2