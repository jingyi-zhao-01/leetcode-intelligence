# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: binary-tree-level-order-traversal-ii
# source_path: LeetCode-Solutions-master/Python/binary-tree-level-order-traversal-ii.py
# solution_class: Solution
# submission_id: 7415e2a215e9a4feb370c9b732daceb0d30bd819
# seed: 1303817831

# Time:  O(n)
# Space: O(n)

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
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

        return result[::-1]