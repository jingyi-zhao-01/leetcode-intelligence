# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: properties-graph
# source_path: LeetCode-Solutions-master/Python/properties-graph.py
# solution_class: Solution
# submission_id: 4d61642b1a474e22f21693a819d1174b06bc268f
# seed: 1224475060

# Time:  O(n^2 * m)
# Space: O(n)

# graph, flood fill, bfs

class Solution(object):
    def numberOfComponents(self, properties, k):
        """
        :type properties: List[List[int]]
        :type k: int
        :rtype: int
        """
        def bfs(u):
            q = [u]
            while q:
                new_q = []
                for u in q:
                    for v in adj[u]:
                        if lookup[v]:
                            continue
                        lookup[v] = True
                        new_q.append(v)
                q = new_q

        p_set = [set(p) for p in properties]
        adj = [[] for _ in xrange(len(properties))]
        for i in xrange(len(p_set)):
            for j in xrange(i+1, len(p_set)):
                if sum(x in p_set[j] for x in p_set[i]) >= k:
                    adj[i].append(j)
                    adj[j].append(i)
        lookup = [False]*len(properties)
        result = 0
        for i in xrange(len(properties)):
            if lookup[i]:
                continue
            bfs(i)
            result += 1
        return result