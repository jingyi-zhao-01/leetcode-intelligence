# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-any-element-has-prime-frequency
# source_path: LeetCode-Solutions-master/Python/check-if-any-element-has-prime-frequency.py
# solution_class: Solution
# submission_id: d610c8b17d3fc9e748f66af434cb6264748f7754
# seed: 3874884882

# Time:  precompute: O(MAX_N)
#        runtime:    O(n)
# Space: O(MAX_N)

import collections


# number theory, freq table
def linear_sieve_of_eratosthenes(n):
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


MAX_N = 100
SPF = linear_sieve_of_eratosthenes(MAX_N)

class Solution(object):
    def checkPrimeFrequency(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cnt = collections.defaultdict(int)
        for x in nums:
            cnt[x] += 1
        return any(SPF[v] == v for v in cnt.itervalues())