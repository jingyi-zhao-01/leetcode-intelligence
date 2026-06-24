# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: univalued-binary-tree
# source_path: LeetCode-Solutions-master/Python/univalued-binary-tree.py
# solution_class: Solution2
# submission_id: 6d2393d75e25bba0f7e1e1ca80bf0452e8f2a2fd
# seed: 4262270953

# Time:  O(n)
# Space: O(h)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution2(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return (not root.left or (root.left.val == root.val and self.isUnivalTree(root.left))) and \
               (not root.right or (root.right.val == root.val and self.isUnivalTree(root.right)))