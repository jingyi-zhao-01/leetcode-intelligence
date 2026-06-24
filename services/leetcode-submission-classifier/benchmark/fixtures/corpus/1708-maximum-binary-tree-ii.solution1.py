# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-binary-tree-ii
# source_path: LeetCode-Solutions-master/Python/maximum-binary-tree-ii.py
# solution_class: Solution
# submission_id: 6924ee1589f63b758ce9e5fe6998e5ec994243bd
# seed: 3947506826

# Time:  O(h)
# Space: O(1)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def insertIntoMaxTree(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return TreeNode(val)

        if val > root.val:
            node = TreeNode(val)
            node.left = root
            return node
        
        curr = root
        while curr.right and curr.right.val > val:
            curr = curr.right
        node = TreeNode(val)
        curr.right, node.left = node, curr.right
        return root