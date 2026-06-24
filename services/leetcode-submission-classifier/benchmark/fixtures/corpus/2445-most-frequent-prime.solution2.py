# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: most-frequent-prime
# source_path: LeetCode-Solutions-master/Python/most-frequent-prime.py
# solution_class: Solution2
# submission_id: 0e1469253dc78abdbafe74ad2b70ff067c637d78
# seed: 3201703545

# Time:  precompute: O(10^MAX_N_M)
#        runtime:    O(n * m * (n + m))
# Space: O(10^MAX_N_M + n * m * (n + m))

import collections


# number theory, freq table
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


MAX_M_N = 6
SPF = linear_sieve_of_eratosthenes(10**MAX_M_N-1)

class Solution2(object):
    def mostFrequentPrime(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        DIRECTIONS = ((1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1))
        def numbers(i, j, di, dj):
            curr = 0
            while 0 <= i < len(mat) and 0 <= j < len(mat[0]):
                curr = curr*10+mat[i][j]
                yield curr
                i, j = i+di, j+dj

        cnt = collections.Counter(x for i in xrange(len(mat)) for j in xrange(len(mat[0])) for di, dj in DIRECTIONS for x in numbers(i, j, di, dj) if x > 10)
        cnt[-1] = 0
        return max((p for p in cnt.iterkeys() if is_prime(p) or p == -1), key=lambda x: (cnt[x], x))