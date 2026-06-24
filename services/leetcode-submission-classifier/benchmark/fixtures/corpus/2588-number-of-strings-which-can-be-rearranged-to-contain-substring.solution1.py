# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-strings-which-can-be-rearranged-to-contain-substring
# source_path: LeetCode-Solutions-master/Python/number-of-strings-which-can-be-rearranged-to-contain-substring.py
# solution_class: Solution
# submission_id: f21af36124e8c5a0cdef2b925eef863591fd8962
# seed: 2372414873

# Time:  O(logn)
# Space: O(1)

# combinatorics, principle of inclusion-exclusion

class Solution(object):
    def stringCount(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9+7
        return (pow(26, n, MOD)-
                (25+25+25+n)*pow(25, n-1, MOD)+      # no l, t, e, ee
                (24+24+24+n+n+0)*pow(24, n-1, MOD)-  # no l|t, l|e, t|e, l|ee, t|ee, e|ee
                (23+n+0+0)*pow(23, n-1, MOD))%MOD    # no l|t|e, l|t|ee, l|e|ee, t|e|ee