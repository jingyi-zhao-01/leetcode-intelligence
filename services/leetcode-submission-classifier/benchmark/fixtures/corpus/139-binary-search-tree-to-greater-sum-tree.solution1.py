# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: binary-search-tree-to-greater-sum-tree
# source_path: LeetCode-Solutions-master/Python/binary-search-tree-to-greater-sum-tree.py
# solution_class: Solution
# submission_id: 9f224e65a281a276b713b49f869400614b1a8085
# seed: 2713950919

# Time:  O(n)
# Space: O(h)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def bstToGstHelper(root, prev):
            if not root:
                return root
            bstToGstHelper(root.right, prev)
            root.val += prev[0]
            prev[0] = root.val
            bstToGstHelper(root.left, prev)
            return root
        
        prev = [0]
        return bstToGstHelper(root, prev)