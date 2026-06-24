# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-path-with-different-adjacent-characters
# source_path: LeetCode-Solutions-master/Python/longest-path-with-different-adjacent-characters.py
# solution_class: Solution2
# submission_id: 21eae003f23ea9eff7dfae172c2da0d55bd78b12
# seed: 1039935242

# Time:  O(n)
# Space: O(w)

import collections


# tree, bfs, topological sort

class Solution2(object):
    def longestPath(self, parent, s):
        """
        :type parent: List[int]
        :type s: str
        :rtype: int
        """
        def iter_dfs(s, adj):
            result = 0
            stk = [(1, (0, [0]))]
            while stk:
                step, args = stk.pop()
                if step == 1:
                    u, ret = args
                    top2 = [0]*2
                    stk.append((4, (top2, ret)))
                    stk.append((2, (u, 0, top2, ret)))
                elif step == 2:
                    u, i, top2, ret = args
                    if i == len(adj[u]):
                        continue
                    ret2 = [0]
                    stk.append((3, (u, i, top2, ret2)))
                    stk.append((1, (adj[u][i], ret2))) 
                elif step == 3:
                    u, i, top2, ret2 = args
                    if s[adj[u][i]] != s[u]:
                        if ret2[0] > top2[0]:
                            top2[0], top2[1] = ret2[0], top2[0]
                        elif ret2[0] > top2[1]:
                            top2[1] = ret2[0]
                    stk.append((2, (u, i+1, top2, ret)))
                elif step == 4:
                    top2, ret = args
                    result = max(result, top2[0]+top2[1]+1)
                    ret[0] = top2[0]+1
            return result
    
        
        adj = [[] for _ in xrange(len(s))]
        for i in xrange(1, len(parent)):
            adj[parent[i]].append(i)
        return iter_dfs(s, adj)