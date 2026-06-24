# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-distinct-path-sum-in-a-binary-tree
# source_path: LeetCode-Solutions-master/Python/maximum-distinct-path-sum-in-a-binary-tree.py
# solution_class: Solution
# submission_id: efbb1727dfb94c99be26ac37289b9fe86488f617
# seed: 420834183

# Time:  O(n^2)
# Space: O(n)

# bfs, iterative dfs

class Solution(object):
    def maxSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def bfs():
            adj = [[]]
            vals = [root.val]
            q = [(root, -1)]
            while q:
                new_q = []
                for u, p in q:
                    vals.append(u.val)
                    adj.append([])
                    i = len(adj)-1
                    if p != -1:
                        adj[i].append(p)
                        adj[p].append(i)
                    for node in (u.left, u.right):
                        if not node:
                            continue
                        new_q.append((node, i))
                q = new_q
            return adj, vals

        def iter_dfs(u):
            result = float("-inf")
            total = 0
            lookup = set()
            stk = [(1, u, -1)]
            while stk:
                step, u, p = stk.pop()
                if step == 1:
                    if vals[u] in lookup:
                        continue
                    stk.append((2, u, p))
                    lookup.add(vals[u])
                    total += vals[u]
                    result = max(result, total)
                    for v in adj[u]:
                        if v == p:
                            continue
                        stk.append((1, v, u))
                elif step == 2:
                    total -= vals[u]
                    lookup.remove(vals[u])
            return result    

        adj, vals = bfs()
        return max(iter_dfs(u) for u in xrange(len(adj)))