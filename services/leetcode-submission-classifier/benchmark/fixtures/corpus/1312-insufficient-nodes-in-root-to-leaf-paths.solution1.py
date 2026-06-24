# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: insufficient-nodes-in-root-to-leaf-paths
# source_path: LeetCode-Solutions-master/Python/insufficient-nodes-in-root-to-leaf-paths.py
# solution_class: Solution
# submission_id: 6d381aaae7bf9b6dcbb9b490195ac478b3714b14
# seed: 4166652595

# Time:  O(n)
# Space: O(h)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sufficientSubset(self, root, limit):
        """
        :type root: TreeNode
        :type limit: int
        :rtype: TreeNode
        """
        if not root:
            return None
        if not root.left and not root.right:
            return None if root.val < limit else root
        root.left = self.sufficientSubset(root.left, limit-root.val)
        root.right = self.sufficientSubset(root.right, limit-root.val)
        if not root.left and not root.right:
            return None
        return root