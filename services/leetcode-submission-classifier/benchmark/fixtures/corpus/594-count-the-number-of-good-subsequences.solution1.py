# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-the-number-of-good-subsequences
# source_path: LeetCode-Solutions-master/Python/count-the-number-of-good-subsequences.py
# solution_class: Solution
# submission_id: 1f14cb05f95520c3b9a27fcdc7644e0a2400fae6
# seed: 3356712087

# Time:  O(26 * n)
# Space: O(n)

import collections


# combinatorics

class Solution(object):
    def countGoodSubsequences(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10**9+7
        fact, inv, inv_fact = [[1]*2 for _ in xrange(3)]
        def nCr(n, k):
            if not (0 <= k <= n):
                return 0
            while len(inv) <= n:  # lazy initialization
                fact.append(fact[-1]*len(inv) % MOD)
                inv.append(inv[MOD%len(inv)]*(MOD-MOD//len(inv)) % MOD)  # https://cp-algorithms.com/algebra/module-inverse.html
                inv_fact.append(inv_fact[-1]*inv[-1] % MOD)
            return (fact[n]*inv_fact[n-k] % MOD) * inv_fact[k] % MOD

        cnt = collections.Counter(s)
        return reduce(lambda total, k: (total+reduce(lambda total, x: total*(1+nCr(x, k))%MOD, cnt.itervalues(), 1)-1)%MOD, xrange(1, max(cnt.itervalues())+1), 0)