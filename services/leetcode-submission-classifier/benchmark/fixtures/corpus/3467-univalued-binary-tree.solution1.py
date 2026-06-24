# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: univalued-binary-tree
# source_path: LeetCode-Solutions-master/Python/univalued-binary-tree.py
# solution_class: Solution
# submission_id: e1c366f86e53bf39b19733ee78fff024fba9ec79
# seed: 19051611

# Time:  O(n)
# Space: O(h)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        s = [root]
        while s:
            node = s.pop()
            if not node:
                continue
            if node.val != root.val:
                return False
            s.append(node.left)
            s.append(node.right)
        return True