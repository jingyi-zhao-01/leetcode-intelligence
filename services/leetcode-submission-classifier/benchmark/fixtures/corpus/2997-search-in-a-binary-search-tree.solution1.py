# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: search-in-a-binary-search-tree
# source_path: LeetCode-Solutions-master/Python/search-in-a-binary-search-tree.py
# solution_class: Solution
# submission_id: 0a92473b1bd6762a3632a3d564ca89669cccb592
# seed: 1236433886

# Time:  O(h)
# Space: O(1)

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        while root and val != root.val:
            if val < root.val:
                root = root.left
            else:
                root = root.right
        return root