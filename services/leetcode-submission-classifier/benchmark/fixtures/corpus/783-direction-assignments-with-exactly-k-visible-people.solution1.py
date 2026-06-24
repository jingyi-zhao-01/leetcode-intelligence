# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: direction-assignments-with-exactly-k-visible-people
# source_path: LeetCode-Solutions-master/Python/direction-assignments-with-exactly-k-visible-people.py
# solution_class: Solution
# submission_id: ed947a96bb20f4a36eba899638b2903e1bfebff7
# seed: 3023002094

# Time:  O(n)
# Space: O(n)

# combinatorics
MOD = 10**9+7
FACT, INV, INV_FACT = [[1]*2 for _ in xrange(3)]
def nCr(n, k):
    while len(INV) <= n:  # lazy initialization
        FACT.append(FACT[-1]*len(INV) % MOD)
        INV.append(INV[MOD%len(INV)]*(MOD-MOD//len(INV)) % MOD)  # https://cp-algorithms.com/algebra/module-inverse.html
        INV_FACT.append(INV_FACT[-1]*INV[-1] % MOD)
    return (FACT[n]*INV_FACT[n-k] % MOD) * INV_FACT[k] % MOD

class Solution(object):
    def countVisiblePeople(self, n, pos, k):
        """
        :type n: int
        :type pos: int
        :type k: int
        :rtype: int
        """
        return (nCr(n-1, k)*2)%MOD