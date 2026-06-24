# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: delete-leaves-with-a-given-value
# source_path: LeetCode-Solutions-master/Python/delete-leaves-with-a-given-value.py
# solution_class: Solution
# submission_id: 105d9951c28a40bc9dbe804253bb1529692a2bc3
# seed: 3115207342

# Time:  O(n)
# Space: O(h)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def removeLeafNodes(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode
        """
        if not root:
            return None
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)
        return None if root.left == root.right and root.val == target else root