# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-valid-paths-in-a-tree
# source_path: LeetCode-Solutions-master/Python/count-valid-paths-in-a-tree.py
# solution_class: Solution2
# submission_id: 44528136ac72f05edaba6432cf5bb62eca0cb75b
# seed: 2586950013

# Time:  O(n)
# Space: O(n)

# number theory, tree dp, iterative dfs

class Solution2(object):
    def countPaths(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
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
            return spf
        
        def is_prime(u):
            return spf[u] == u

        def dfs(u, p):
            cnt = [1-is_prime(u+1), is_prime(u+1)]
            for v in adj[u]:
                if v == p:
                    continue
                new_cnt = dfs(v, u)
                result[0] += cnt[0]*new_cnt[1]+cnt[1]*new_cnt[0]
                if is_prime(u+1):
                    cnt[1] += new_cnt[0]
                else:
                    cnt[0] += new_cnt[0]
                    cnt[1] += new_cnt[1]
            return cnt

        spf = linear_sieve_of_eratosthenes(n)
        adj = [[] for _ in xrange(n)]
        for u, v in edges:
            u, v = u-1, v-1
            adj[u].append(v)
            adj[v].append(u)
        result = [0]
        dfs(0, -1)
        return result[0]