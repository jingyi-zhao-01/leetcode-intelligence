# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-difference-between-node-and-ancestor
# source_path: LeetCode-Solutions-master/Python/maximum-difference-between-node-and-ancestor.py
# solution_class: Solution2
# submission_id: b21f9922380a7a40ac6e3a3ac67b50dabce37405
# seed: 253138984

# Time:  O(n)
# Space: O(h)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# iterative stack solution

class Solution2(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def maxAncestorDiffHelper(node, mx, mn): 
            if not node:
                return 0
            result = max(mx-node.val, node.val-mn)
            mx = max(mx, node.val)
            mn = min(mn, node.val)
            result = max(result, maxAncestorDiffHelper(node.left, mx, mn))
            result = max(result, maxAncestorDiffHelper(node.right, mx, mn))
            return result

        return maxAncestorDiffHelper(root, 0, float("inf"))