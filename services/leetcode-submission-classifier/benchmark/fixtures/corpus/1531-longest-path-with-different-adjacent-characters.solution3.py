# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-path-with-different-adjacent-characters
# source_path: LeetCode-Solutions-master/Python/longest-path-with-different-adjacent-characters.py
# solution_class: Solution3
# submission_id: ef83ce6d76e7279939465ff2b3b3009b9b9c2b52
# seed: 750940766

# Time:  O(n)
# Space: O(w)

import collections


# tree, bfs, topological sort

class Solution3(object):
    def longestPath(self, parent, s):
        """
        :type parent: List[int]
        :type s: str
        :rtype: int
        """
        def dfs(s, adj, u, result):
            top2 = [0]*2
            for v in adj[u]:
                l = dfs(s, adj, v, result)
                if s[v] == s[u]:
                    continue
                if l > top2[0]:
                    top2[0], top2[1] = l, top2[0]
                elif l > top2[1]:
                    top2[1] = l
            result[0] = max(result[0], top2[0]+top2[1]+1)
            return top2[0]+1
    
        
        adj = [[] for _ in xrange(len(s))]
        for i in xrange(1, len(parent)):
            adj[parent[i]].append(i)
        result = [0]
        dfs(s, adj, 0, result)
        return result[0]