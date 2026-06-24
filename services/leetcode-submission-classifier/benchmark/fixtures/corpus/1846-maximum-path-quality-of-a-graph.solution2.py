# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-path-quality-of-a-graph
# source_path: LeetCode-Solutions-master/Python/maximum-path-quality-of-a-graph.py
# solution_class: Solution2
# submission_id: 64b109af138cf5594c80b313e3a7c8ffd39eb324
# seed: 4293979729

# Time: O(|V| + |E| + 4^(maxTime/min(times))) = O(|V| + |E| + 4^10)
# Time: O(|V| + |E|)

class Solution2(object):
    def maximalPathQuality(self, values, edges, maxTime):
        """
        :type values: List[int]
        :type edges: List[List[int]]
        :type maxTime: int
        :rtype: int
        """
        def dfs(values, adj, u, time, total, lookup, lookup2, result):
            lookup[u] += 1
            if lookup[u] == 1:
                total += values[u]
            if not u:
                result[0] = max(result[0], total)
            for v, t in adj[u]:
                if (u, v) in lookup2 or time < t:  # same directed edge won't be visited twice
                    continue
                lookup2.add((u, v))
                dfs(values, adj, v, time-t, total, lookup, lookup2, result)
                lookup2.remove((u, v))
            lookup[u] -= 1

        adj = [[] for _ in xrange(len(values))]
        for u, v, t in edges:
            adj[u].append((v, t))
            adj[v].append((u, t))
        result = [0]
        dfs(values, adj, 0, maxTime, 0, [0]*len(adj), set(), result)
        return result[0]