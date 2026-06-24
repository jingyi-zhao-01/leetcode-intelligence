# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: binary-tree-right-side-view
# source_path: LeetCode-Solutions-master/Python/binary-tree-right-side-view.py
# solution_class: Solution2
# submission_id: a8ed2d1c4aca10d9191b008193a2ceb87924ede9
# seed: 2418086531

# Time:  O(n)
# Space: O(h)

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution2(object):
    # @param root, a tree node
    # @return a list of integers
    def rightSideView(self, root):
        if root is None:
            return []

        result, current = [], [root]
        while current:
            next_level = []
            for node in current:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)                
            result.append(node.val)
            current = next_level

        return result