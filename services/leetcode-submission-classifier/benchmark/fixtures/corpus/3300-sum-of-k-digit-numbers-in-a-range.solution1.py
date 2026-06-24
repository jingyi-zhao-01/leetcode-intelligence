# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sum-of-k-digit-numbers-in-a-range
# source_path: LeetCode-Solutions-master/Python/sum-of-k-digit-numbers-in-a-range.py
# solution_class: Solution
# submission_id: a3d47ea583820252e2dd949f12e3122966607712
# seed: 2393447817

# Time:  O(logr)
# Space: O(1)

# math

class Solution(object):
    def sumOfNumbers(self, l, r, k):
        """
        :type l: int
        :type r: int
        :type k: int
        :rtype: int
        """
        def invmod(x, MOD):
            return pow(x, MOD-2, MOD)
    
        MOD = 10**9+7
        return (((((r+l)*(r-l+1)//2)*pow(r-l+1, k-1, MOD))%MOD)*((((pow(10, k, MOD)-1)%MOD)*invmod(10-1, MOD))%MOD))%MOD