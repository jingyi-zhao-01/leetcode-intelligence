# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-vowels-permutation
# source_path: LeetCode-Solutions-master/Python/count-vowels-permutation.py
# solution_class: Solution2
# submission_id: 2349189ba191ccd346b33326d29d5d4e6ed41090
# seed: 123823683

# Time:  O(logn)
# Space: O(1)

import itertools

class Solution2(object):
    def countVowelPermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7
        a, e, i, o, u = 1, 1, 1, 1, 1
        for _ in xrange(1, n):
            a, e, i, o, u = (e+i+u) % MOD, (a+i) % MOD, (e+o) % MOD, i, (i+o) % MOD
        return (a+e+i+o+u) % MOD