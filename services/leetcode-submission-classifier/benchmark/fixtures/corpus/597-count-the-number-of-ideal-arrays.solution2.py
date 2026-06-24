# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-the-number-of-ideal-arrays
# source_path: LeetCode-Solutions-master/Python/count-the-number-of-ideal-arrays.py
# solution_class: Solution2
# submission_id: 6ece4f51f787da6870d888e6b2a5b83fd083ca93
# seed: 1389960815

# Time:  O(sqrt(m) + n + m * (logm + pi(sqrt(m)))) = O(sqrt(m) + n + m * (logm + sqrt(m)/log(sqrt(m)))), pi(n) = number of primes in a range [1, n] = O(n/logn) by prime number theorem, see https://en.wikipedia.org/wiki/Prime_number_theorem
# Space: O(sqrt(m) + n + logm)

import collections


# dp, factorization, combinatorics

class Solution2(object):
    def idealArrays(self, n, maxValue):
        """
        :type n: int
        :type maxValue: int
        :rtype: int
        """
        MOD = 10**9+7
        fact, inv, inv_fact = [[1]*2 for _ in xrange(3)]
        def nCr(n, k):
            while len(inv) <= n:  # lazy initialization
                fact.append(fact[-1]*len(inv) % MOD)
                inv.append(inv[MOD%len(inv)]*(MOD-MOD//len(inv)) % MOD)  # https://cp-algorithms.com/algebra/module-inverse.html
                inv_fact.append(inv_fact[-1]*inv[-1] % MOD)
            return (fact[n]*inv_fact[n-k] % MOD) * inv_fact[k] % MOD

        result = 0
        dp = collections.Counter(xrange(1, maxValue+1))
        for i in xrange(n): 
            new_dp = collections.Counter()
            total = 0
            for x, c in dp.iteritems():
                total = (total+c)%MOD
                for y in xrange(x+x, maxValue+1, x): 
                    new_dp[y] += c
            result = (result+total*nCr(n-1, i))%MOD
            dp = new_dp
        return result