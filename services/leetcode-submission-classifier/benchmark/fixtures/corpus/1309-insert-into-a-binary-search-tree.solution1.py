# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: insert-into-a-binary-search-tree
# source_path: LeetCode-Solutions-master/Python/insert-into-a-binary-search-tree.py
# solution_class: Solution
# submission_id: ce856e88b1411312cb33e84fc355868f95e8323c
# seed: 1208162738

# Time:  O(h)
# Space: O(1)

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        curr, parent = root, None
        while curr:
            parent = curr
            if val <= curr.val:
                curr = curr.left
            else:
                curr = curr.right
        if not parent:
            root = TreeNode(val)
        elif val <= parent.val:
            parent.left = TreeNode(val)
        else:
            parent.right = TreeNode(val)
        return root