# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-valid-paths-in-a-tree
# source_path: LeetCode-Solutions-master/Python/count-valid-paths-in-a-tree.py
# solution_class: Solution3
# submission_id: c69165d3888b4b44b80b06031145ba519aac025f
# seed: 1345428104

# Time:  O(n)
# Space: O(n)

# number theory, tree dp, iterative dfs

class Solution3(object):
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

        spf = linear_sieve_of_eratosthenes(n)
        uf = UnionFind(n)
        for u, v in edges:
            u, v = u-1, v-1
            if is_prime(u+1) == is_prime(v+1) == False:
                uf.union_set(u, v) 
        result = 0
        cnt = [1]*n
        for u, v in edges:
            u, v = u-1, v-1
            if is_prime(u+1) == is_prime(v+1):
                continue
            if not is_prime(u+1):
                u, v = v, u
            result += cnt[u]*uf.total(v)
            cnt[u] += uf.total(v)
        return result