# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-minimum-diameter-after-merging-two-trees
# source_path: LeetCode-Solutions-master/Python/find-minimum-diameter-after-merging-two-trees.py
# solution_class: Solution
# submission_id: 301f691e487fe829fcde832d51ff286c65c5962c
# seed: 1263996782

# Time:  O(n + m)
# Space: O(n + m)

# iterative dfs, tree diameter

class Solution(object):
    def minimumDiameterAfterMerge(self, edges1, edges2):
        """
        :type edges1: List[List[int]]
        :type edges2: List[List[int]]
        :rtype: int
        """
        def ceil_divide(a, b):
            return (a+b-1)//2
    
        def tree_diameter(edges):
            def iter_dfs():
                result = 0
                stk = [(1, (0, -1, [0]))]
                while stk:
                    step, args = stk.pop()
                    if step == 1:
                        u, p, ret = args
                        for v in reversed(adj[u]):
                            if v == p:
                                continue
                            ret2 = [0]
                            stk.append((2, (ret2, ret)))
                            stk.append((1, (v, u, ret2)))
                    elif step == 2:
                        ret2, ret = args
                        result = max(result, ret[0]+(ret2[0]+1))
                        ret[0] = max(ret[0], ret2[0]+1)
                return result
            
            adj = [[] for _ in xrange(len(edges)+1)]
            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)
            return iter_dfs()
        
        d1 = tree_diameter(edges1)
        d2 = tree_diameter(edges2)
        return max(ceil_divide(d1, 2)+1+ceil_divide(d2, 2), d1, d2)