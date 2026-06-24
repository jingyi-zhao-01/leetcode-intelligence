# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-path-quality-of-a-graph
# source_path: LeetCode-Solutions-master/Python/maximum-path-quality-of-a-graph.py
# solution_class: Solution3
# submission_id: fefcf8945689278fb9b285ca9f59d91244acfdb0
# seed: 57318405

# Time: O(|V| + |E| + 4^(maxTime/min(times))) = O(|V| + |E| + 4^10)
# Time: O(|V| + |E|)

class Solution3(object):
    def maximalPathQuality(self, values, edges, maxTime):
        """
        :type values: List[int]
        :type edges: List[List[int]]
        :type maxTime: int
        :rtype: int
        """
        def dfs(values, adj, u, time, total, lookup, lookup2):
            lookup[u] += 1
            if lookup[u] == 1:
                total += values[u]
            result = total if not u else 0
            for v, t in adj[u]:
                if (u, v) in lookup2 or time < t:  # same directed edge won't be visited twice
                    continue
                lookup2.add((u, v))
                result = max(result, dfs(values, adj, v, time-t, total, lookup, lookup2))
                lookup2.remove((u, v))
            lookup[u] -= 1
            return result

        adj = [[] for _ in xrange(len(values))]
        for u, v, t in edges:
            adj[u].append((v, t))
            adj[v].append((u, t))
        return dfs(values, adj, 0, maxTime, 0, [0]*len(adj), set())