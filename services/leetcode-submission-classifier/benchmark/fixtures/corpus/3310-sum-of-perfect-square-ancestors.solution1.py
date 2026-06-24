# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sum-of-perfect-square-ancestors
# source_path: LeetCode-Solutions-master/Python/sum-of-perfect-square-ancestors.py
# solution_class: Solution
# submission_id: 47ce1f2a3a9f93bf5bd4c8bc22800c9906ee8a60
# seed: 322380049

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

class Solution(object):
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

        def iter_dfs():
            result = 0
            stk = [(1, (0, -1))]
            while stk:
                step, args = stk.pop()
                if step == 1:
                    u, p = args
                    x = prime_factors(nums[u])
                    result += cnt[x]
                    cnt[x] += 1
                    stk.append((3, (x,)))
                    stk.append((2, (u, p, 0)))
                elif step == 2:
                    u, p, i = args
                    if i == len(adj[u]):
                        continue
                    stk.append((2, (u, p, i+1)))
                    v = adj[u][i]
                    if v == p:
                        continue
                    stk.append((1, (v, u)))
                elif step == 3:
                    x = args[0]
                    cnt[x] -= 1
            return result

        adj = [[] for _ in xrange(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        cnt = collections.defaultdict(int)
        return iter_dfs()