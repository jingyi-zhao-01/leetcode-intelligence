# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-the-number-of-arrays-with-k-matching-adjacent-elements
# source_path: LeetCode-Solutions-master/Python/count-the-number-of-arrays-with-k-matching-adjacent-elements.py
# solution_class: Solution
# submission_id: 5bf80e601f5f9b1e1c453af5c7fd7bc21f8fb929
# seed: 4108265764

# Time:  O(n + logm)
# Space: O(n)

# combinatorics, fast exponentiation
MOD = 10**9+7
FACT, INV, INV_FACT = [[1]*2 for _ in xrange(3)]
def nCr(n, k):
    while len(INV) <= n:  # lazy initialization
        FACT.append(FACT[-1]*len(INV) % MOD)
        INV.append(INV[MOD%len(INV)]*(MOD-MOD//len(INV)) % MOD)  # https://cp-algorithms.com/algebra/module-inverse.html
        INV_FACT.append(INV_FACT[-1]*INV[-1] % MOD)
    return (FACT[n]*INV_FACT[n-k] % MOD) * INV_FACT[k] % MOD

class Solution(object):
    def countGoodArrays(self, n, m, k):
        """
        :type n: int
        :type m: int
        :type k: int
        :rtype: int
        """
        return (nCr(n-1, k)*(m*pow(m-1, (n-1)-k, MOD)))%MOD