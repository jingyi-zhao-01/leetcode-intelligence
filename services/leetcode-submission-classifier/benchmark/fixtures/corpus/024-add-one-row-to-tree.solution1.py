# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: add-one-row-to-tree
# source_path: LeetCode-Solutions-master/Python/add-one-row-to-tree.py
# solution_class: Solution
# submission_id: b66f66cec60872a28b18169b375052e9f68f5a17
# seed: 3637880147

# Time:  O(n)
# Space: O(h)

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d in (0, 1):
            node = TreeNode(v)
            if d == 1:
                node.left = root
            else:
                node.right = root
            return node
        if root and d >= 2:
            root.left = self.addOneRow(root.left,  v, d-1 if d > 2 else 1)
            root.right = self.addOneRow(root.right, v, d-1 if d > 2 else 0)
        return root