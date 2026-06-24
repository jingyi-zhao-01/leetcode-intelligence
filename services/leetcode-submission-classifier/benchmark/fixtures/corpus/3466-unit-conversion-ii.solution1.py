# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: unit-conversion-ii
# source_path: LeetCode-Solutions-master/Python/unit-conversion-ii.py
# solution_class: Solution
# submission_id: 991ca07247fddb755f735aeaf580d7e5c5f9df0a
# seed: 2665273670

# Time:  O(n + qlogm)
# Space: O(n)

# bfs, fast exponentiation

class Solution(object):
    def queryConversions(self, conversions, queries):
        """
        :type conversions: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        MOD = 10**9+7
        def divmod(a, b):
            return (a*pow(b, MOD-2, MOD))%MOD

        def unit():
            adj = [[] for _ in xrange(len(conversions)+1)]
            for u, v, w in conversions:
                adj[u].append((v, w))
            result = [0]*len(adj)
            result[0] = 1
            q = [0]
            while q:
                new_q = []
                for u in q:
                    for v, w in adj[u]:
                        result[v] = (result[u]*w)%MOD
                        new_q.append(v)
                q = new_q
            return result
        
        lookup = unit()
        return [divmod(lookup[b], lookup[a]) for a, b in queries]