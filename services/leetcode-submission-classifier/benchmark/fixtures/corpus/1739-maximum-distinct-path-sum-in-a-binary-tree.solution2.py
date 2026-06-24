# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-distinct-path-sum-in-a-binary-tree
# source_path: LeetCode-Solutions-master/Python/maximum-distinct-path-sum-in-a-binary-tree.py
# solution_class: Solution2
# submission_id: b1569b3a858e22ae79f0f885772c9d5678b1de8b
# seed: 361675433

# Time:  O(n^2)
# Space: O(n)

# bfs, iterative dfs

class Solution2(object):
    def maxSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def dfs1(u, p):
            vals.append(u.val)
            adj.append([])
            i = len(adj)-1
            if p != -1:
                adj[i].append(p)
                adj[p].append(i)
            for node in (u.left, u.right):
                if not node:
                    continue
                dfs1(node, i)
        
        def dfs2(u, p):
            if vals[u] in lookup:
                return float("-inf")
            lookup.add(vals[u])
            mx = 0
            for v in adj[u]:
                if v == p:
                    continue
                mx = max(mx, dfs2(v, u))
            lookup.remove(vals[u])
            return vals[u]+mx
            
        adj, vals = [], []
        dfs1(root, -1)
        lookup = set()
        return max(dfs2(u, -1) for u in xrange(len(adj)))