# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-the-number-of-square-free-subsets
# source_path: LeetCode-Solutions-master/Python/count-the-number-of-square-free-subsets.py
# solution_class: Solution
# submission_id: 1d67b3e0e12085a4ff959218cacd81f979692897
# seed: 696421334

# Time:  O(n + m * 2^p)
# Space: O(m * 2^p)

import collections


# number theory, combinatorics, bitmasks, dp

class Solution(object):
    def squareFreeSubsets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
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
            return primes

        MAX_NUM = max(nums)
        PRIMES = linear_sieve_of_eratosthenes(MAX_NUM)
        MASKS = [0]*(MAX_NUM+1)
        for x in xrange(MAX_NUM+1):
            y = x
            for i, p in enumerate(PRIMES):
                if y%p:
                    continue
                if y%p**2 == 0:
                    MASKS[x] = 0
                    break
                MASKS[x] |= (1<<i)
                y //= p
        MOD = 10**9+7

        cnt = collections.Counter(nums)
        arr = [x for x in cnt.iterkeys() if x != 1]
        dp = [1]*(1<<len(PRIMES))
        for x in arr:
            if not MASKS[x]:
                continue
            for mask in reversed(xrange(len(dp))):
                 if MASKS[x]&mask == 0:
                    dp[mask|MASKS[x]] = (dp[mask|MASKS[x]]+cnt[x]*dp[mask])%MOD
        return (dp[-1]*pow(2, cnt[1], MOD)-1)%MOD if 1 in cnt else (dp[-1]-1)%MOD