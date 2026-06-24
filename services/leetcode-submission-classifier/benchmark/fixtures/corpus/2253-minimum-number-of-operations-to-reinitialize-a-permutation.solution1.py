# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-number-of-operations-to-reinitialize-a-permutation
# source_path: LeetCode-Solutions-master/Python/minimum-number-of-operations-to-reinitialize-a-permutation.py
# solution_class: Solution
# submission_id: dbaee2243c16364bb29226814bc60c06c8c914e9
# seed: 2544252573

# Time:  O(sqrt(n))
# Space: O(sqrt(n))

class Solution(object):
    def reinitializePermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        # reference: https://cp-algorithms.com/algebra/discrete-log.html
        def discrete_log(a, b, m):
            a %= m
            b %= m
            n = int(m**0.5)+1
            an = pow(a, n, m)
            vals = {}
            curr = b
            for q in xrange(n+1):
                vals[curr] = q
                curr = curr*a % m
            curr = 1
            for p in xrange(1, n+1):
                curr = curr*an % m
                if curr in vals:
                    return n*p-vals[curr]
            return -1

        return 1+discrete_log(2, n//2, n-1)  # find min x s.t. 2^x mod (n-1) = n/2, result is x + 1