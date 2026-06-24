# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sum-of-perfect-square-ancestors
# source_path: LeetCode-Solutions-master/Python/sum-of-perfect-square-ancestors.py
# solution_class: Solution2
# submission_id: 7821b9686ac98bc9d961f39a534383b20ed45c1c
# seed: 100028590

# Time:  precompute: O(r)
#        runtime:    O(nlogx)
# Space: O(r + n)

import collections


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


MAX_NUMS = 10**5
SPF = linear_sieve_of_eratosthenes(MAX_NUMS)

# number theory, iterative dfs, freq table

class Solution2(object):
    def sumOfAncestors(self, n, edges, nums):
        """
        :type n: int
        :type edges: List[List[int]]
        :type nums: List[int]
        :rtype: int
        """
        def prime_factors(x):
            result = 1
            while x != 1:
                if result%SPF[x] == 0:
                    result //= SPF[x]
                else:
                    result *= SPF[x]
                x //= SPF[x]
            return result

        def dfs(u, p):
            x = prime_factors(nums[u])
            result = cnt[x]
            cnt[x] += 1
            for v in adj[u]:
                if v == p:
                    continue
                result += dfs(v, u)
            cnt[x] -= 1
            return result

        adj = [[] for _ in xrange(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        cnt = collections.defaultdict(int)
        return dfs(0, -1)