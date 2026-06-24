# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-number-of-operations-to-sort-a-binary-tree-by-level
# source_path: LeetCode-Solutions-master/Python/minimum-number-of-operations-to-sort-a-binary-tree-by-level.py
# solution_class: Solution
# submission_id: 7bcf1983f43079e23efa5ceb7c6dea9420134be3
# seed: 1284534956

# Time:  O(nlogn)
# Space: O(w)

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        pass


# bfs, sort

class Solution(object):
    def minimumOperations(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        result = 0
        q = [root]
        while q:
            new_q = []
            for node in q:
                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right)
            idx = range(len(q))
            idx.sort(key=lambda x: q[x].val)
            for i in xrange(len(q)):
                while idx[i] != i:
                    idx[idx[i]], idx[i] = idx[i], idx[idx[i]]
                    result += 1
            q = new_q
        return result