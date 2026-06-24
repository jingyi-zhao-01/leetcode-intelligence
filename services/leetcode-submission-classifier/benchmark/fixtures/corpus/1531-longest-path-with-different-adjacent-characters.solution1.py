# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-path-with-different-adjacent-characters
# source_path: LeetCode-Solutions-master/Python/longest-path-with-different-adjacent-characters.py
# solution_class: Solution
# submission_id: dfc160431e7e321ac6b414449d7f4d8de1827003
# seed: 4222167243

# Time:  O(n)
# Space: O(w)

import collections


# tree, bfs, topological sort

class Solution(object):
    def longestPath(self, parent, s):
        """
        :type parent: List[int]
        :type s: str
        :rtype: int
        """
        def topological_sort(s, adj, in_degree):
            result = 1
            top2 = collections.defaultdict(lambda:[0]*2)
            q =  [(i, 1) for i, d in enumerate(in_degree) if not d]
            while q:
                new_q = []
                for (u, l) in q:
                    for v in adj[u]:
                        if s[v] != s[u]:
                            if l > top2[v][0]:
                                top2[v][0], top2[v][1] = l, top2[v][0]
                            elif l > top2[v][1]:
                                top2[v][1] = l
                        in_degree[v] -= 1
                        if in_degree[v]:
                            continue
                        new_q.append((v, top2[v][0]+1))
                        result = max(result, top2[v][0]+top2[v][1]+1)
                        del top2[v]
                q = new_q
            return result

        adj = [[] for _ in xrange(len(s))]
        in_degree = [0]*len(s)
        for i in xrange(1, len(parent)):
            adj[i].append(parent[i])
            in_degree[parent[i]] += 1
        return topological_sort(s, adj, in_degree)