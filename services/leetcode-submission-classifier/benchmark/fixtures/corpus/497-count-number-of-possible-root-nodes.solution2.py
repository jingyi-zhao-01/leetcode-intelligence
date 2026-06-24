# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-number-of-possible-root-nodes
# source_path: LeetCode-Solutions-master/Python/count-number-of-possible-root-nodes.py
# solution_class: Solution2
# submission_id: 254fb3261ec85ba15b5ff4e3661daaf7585070a5
# seed: 1738998621

# Time:  O(n) 
# Space: O(h)

import collections


# iterative dfs

class Solution2(object):
    def rootCount(self, edges, guesses, k):
        """
        :type edges: List[List[int]]
        :type guesses: List[List[int]]
        :type k: int
        :rtype: int
        """
        def dfs(u, p):
            cnt = int((p, u) in lookup)
            for v in adj[u]:
                if v == p:
                    continue
                cnt += dfs(v, u)
            return cnt
        
        def dfs2(u, p, curr):
            if (p, u) in lookup:
                curr -= 1
            if (u, p) in lookup:
                curr += 1
            cnt = int(curr >= k)
            for v in adj[u]:
                if v == p:
                    continue
                cnt += dfs2(v, u, curr)
            return cnt

        adj = collections.defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        lookup = {(u, v) for u, v in guesses}
        curr = dfs(0, -1)
        return dfs2(0, -1, curr)