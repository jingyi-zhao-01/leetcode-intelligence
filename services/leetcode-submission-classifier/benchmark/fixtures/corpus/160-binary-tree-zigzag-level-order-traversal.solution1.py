# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: binary-tree-zigzag-level-order-traversal
# source_path: LeetCode-Solutions-master/Python/binary-tree-zigzag-level-order-traversal.py
# solution_class: Solution
# submission_id: 7ee8275a648a339310e244225504c66094d81d94
# seed: 3815305327

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
    def zigzagLevelOrder(self, root):
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
            result.append(vals[::-1] if len(result) % 2 else vals)
            current = next_level
        return result