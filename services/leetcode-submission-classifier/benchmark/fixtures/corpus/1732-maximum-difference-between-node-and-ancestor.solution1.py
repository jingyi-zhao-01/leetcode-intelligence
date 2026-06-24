# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-difference-between-node-and-ancestor
# source_path: LeetCode-Solutions-master/Python/maximum-difference-between-node-and-ancestor.py
# solution_class: Solution
# submission_id: 8837be4c04e56435d25590e45f2f3368af2db9f1
# seed: 3594746363

# Time:  O(n)
# Space: O(h)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# iterative stack solution

class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = 0
        stack = [(root, 0, float("inf"))]
        while stack:
            node, mx, mn = stack.pop()
            if not node:
                continue
            result = max(result, mx-node.val, node.val-mn)
            mx = max(mx, node.val)
            mn = min(mn, node.val)
            stack.append((node.left, mx, mn))
            stack.append((node.right, mx, mn))
        return result