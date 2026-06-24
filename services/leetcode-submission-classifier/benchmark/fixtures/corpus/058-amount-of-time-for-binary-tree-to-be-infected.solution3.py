# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: amount-of-time-for-binary-tree-to-be-infected
# source_path: LeetCode-Solutions-master/Python/amount-of-time-for-binary-tree-to-be-infected.py
# solution_class: Solution3
# submission_id: 4c687b0b9bc4654b78eddc8d6cc11748c5371adf
# seed: 3456656000

# Time:  O(n)
# Space: O(h)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        pass


# iterative dfs, tree dp

class Solution3(object):
    def amountOfTime(self, root, start):
        """
        :type root: Optional[TreeNode]
        :type start: int
        :rtype: int
        """
        def bfs(root):
            adj = collections.defaultdict(list)
            q = [root]
            while q:
                new_q = []
                for u in q:
                    for v in (u.left, u.right):
                        if v is None:
                            continue
                        adj[u.val].append(v.val)
                        adj[v.val].append(u.val)
                        new_q.append(v)
                q = new_q
            return adj

        def bfs2(adj, start):
            result = -1
            q = [start]
            lookup = {start}
            while q:
                new_q = []
                for u in q:
                    for v in adj[u]:
                        if v in lookup:
                            continue
                        lookup.add(v)
                        new_q.append(v)
                q = new_q
                result += 1
            return result

        adj = bfs(root)
        return bfs2(adj, start)