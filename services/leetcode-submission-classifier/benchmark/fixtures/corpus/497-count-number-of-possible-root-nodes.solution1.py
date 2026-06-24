# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-number-of-possible-root-nodes
# source_path: LeetCode-Solutions-master/Python/count-number-of-possible-root-nodes.py
# solution_class: Solution
# submission_id: 53cd85272198d89a9a0792608f729873c106dc21
# seed: 3081290223

# Time:  O(n) 
# Space: O(h)

import collections


# iterative dfs

class Solution(object):
    def rootCount(self, edges, guesses, k):
        """
        :type edges: List[List[int]]
        :type guesses: List[List[int]]
        :type k: int
        :rtype: int
        """
        def iter_dfs():
            result = 0
            stk = [(0, -1)]
            while stk:
                u, p = stk.pop()
                result += int((p, u) in lookup)
                for v in adj[u]:
                    if v == p:
                        continue
                    stk.append((v, u))
            return result
        
        def iter_dfs2(curr):
            result = 0
            stk = [(0, -1, curr)]
            while stk:
                u, p, curr = stk.pop()
                if (p, u) in lookup:
                    curr -= 1
                if (u, p) in lookup:
                    curr += 1
                result += int(curr >= k)
                for v in adj[u]:
                    if v == p:
                        continue
                    stk.append((v, u, curr))
            return result

        adj = collections.defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        lookup = {(u, v) for u, v in guesses}
        curr = iter_dfs()
        return iter_dfs2(curr)