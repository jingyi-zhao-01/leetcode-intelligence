# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: permutation-sequence
# source_path: LeetCode-Solutions-master/Python/permutation-sequence.py
# solution_class: Solution
# submission_id: 817c4fa5f258df2403c6c3516ca1ae1105800469
# seed: 1873195635

# Time:  O(n^2)
# Space: O(n)

import math

# Cantor ordering solution

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        seq, k, fact = "", k - 1, math.factorial(n - 1)
        perm = [i for i in xrange(1, n + 1)]
        for i in reversed(xrange(n)):
            curr = perm[k / fact]
            seq += str(curr)
            perm.remove(curr)
            if i > 0:
                k %= fact
                fact /= i
        return seq