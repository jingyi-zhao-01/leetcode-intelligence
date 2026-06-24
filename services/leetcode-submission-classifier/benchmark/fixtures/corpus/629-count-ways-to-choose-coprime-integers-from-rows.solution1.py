# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-ways-to-choose-coprime-integers-from-rows
# source_path: LeetCode-Solutions-master/Python/count-ways-to-choose-coprime-integers-from-rows.py
# solution_class: Solution
# submission_id: fb605c37f435c1dbac2b0a78a540bdff3ad90b97
# seed: 3782814351

# Time:  O(n * (m + rlogr)), r = max(max(row) for row in mat)
# Space: O(r)

import collections


# dp, number theory, mobius function, principle of inclusion-exclusion, freq table

class Solution(object):
    def countCoprime(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        MOD = 10**9+7
        def linear_sieve_of_eratosthenes(n):  # Time: O(n), Space: O(n)
            primes = []
            spf = [-1]*(n+1)  # the smallest prime factor
            for i in xrange(2, n+1):
                if spf[i] == -1:
                    spf[i] = i
                    primes.append(i)
                for p in primes:
                    if i*p > n or p > spf[i]:
                        break
                    spf[i*p] = p
            return spf

        # https://www.geeksforgeeks.org/program-for-mobius-function-set-2/
        def mobius(spf):  # Time: O(n), Space: O(n)
            mu = [0]*len(spf)
            for i in xrange(1, len(mu)):
                mu[i] = 1 if i == 1 else 0 if spf[i//spf[i]] == spf[i] else -mu[i//spf[i]]
            return mu

        mx = max(max(row) for row in mat)
        mu = mobius(linear_sieve_of_eratosthenes(mx))
        dp = [1]*(mx+1)
        for row in mat:
            cnt = collections.defaultdict(int)
            for x in row:
                cnt[x] += 1
            for i in xrange(1, mx+1):
                dp[i] = (dp[i]*reduce(lambda accu, x: (accu+x)%MOD, (cnt[j] for j in xrange(i, mx+1, i)), 0))%MOD
        return reduce(lambda accu, x: (accu+x)%MOD, (dp[i]*mu[i] for i in xrange(1, mx+1)), 0)