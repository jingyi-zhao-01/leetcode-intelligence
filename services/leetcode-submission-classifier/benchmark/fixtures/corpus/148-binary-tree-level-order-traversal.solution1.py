# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: binary-tree-level-order-traversal
# source_path: LeetCode-Solutions-master/Python/binary-tree-level-order-traversal.py
# solution_class: Solution
# submission_id: 2fc2176a00251dd22499574c7c5902d00e441c9f
# seed: 1826588280

# Time:  O(n)
# Space: O(n)

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        if root is None:
            return []
        result, current = [], [root]
        while current:
            next_level, vals = [], []
            for node in current:
                vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            current = next_level
            result.append(vals)
        return result