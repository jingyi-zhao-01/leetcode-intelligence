# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: symmetric-tree
# source_path: LeetCode-Solutions-master/Python/symmetric-tree.py
# solution_class: Solution
# submission_id: 9b299bdadec6671bb40161b61e187a97cc609127
# seed: 1475408685

# Time:  O(n)
# Space: O(h), h is height of binary tree
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Iterative solution

class Solution(object):
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if root is None:
            return True
        stack = []
        stack.append(root.left)
        stack.append(root.right)

        while stack:
            p, q = stack.pop(), stack.pop()

            if p is None and q is None:
                continue

            if p is None or q is None or p.val != q.val:
                return False

            stack.append(p.left)
            stack.append(q.right)

            stack.append(p.right)
            stack.append(q.left)

        return True