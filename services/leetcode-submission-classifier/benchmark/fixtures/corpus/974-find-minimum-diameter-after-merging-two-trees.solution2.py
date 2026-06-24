# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-minimum-diameter-after-merging-two-trees
# source_path: LeetCode-Solutions-master/Python/find-minimum-diameter-after-merging-two-trees.py
# solution_class: Solution2
# submission_id: a2b06cd4ddb0897200a87b5eea3d28eeb4a3c145
# seed: 1084433629

# Time:  O(n + m)
# Space: O(n + m)

# iterative dfs, tree diameter

class Solution2(object):
    def minimumDiameterAfterMerge(self, edges1, edges2):
        """
        :type edges1: List[List[int]]
        :type edges2: List[List[int]]
        :rtype: int
        """
        def ceil_divide(a, b):
            return (a+b-1)//2
    
        def tree_diameter(edges):
            def dfs(u, p):
                mx = 0
                for v in adj[u]:
                    if v == p:
                        continue
                    curr = dfs(v, u)
                    result[0] = max(result[0], mx+(curr+1))
                    mx = max(mx, curr+1)
                return mx
            
            adj = [[] for _ in xrange(len(edges)+1)]
            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)
            result = [0]
            dfs(0, -1)
            return result[0]
        
        d1 = tree_diameter(edges1)
        d2 = tree_diameter(edges2)
        return max(ceil_divide(d1, 2)+1+ceil_divide(d2, 2), d1, d2)