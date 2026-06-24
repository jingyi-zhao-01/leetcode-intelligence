# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: binary-tree-upside-down
# source_path: LeetCode-Solutions-master/Python/binary-tree-upside-down.py
# solution_class: Solution
# submission_id: 26f9a95d7cea261bbf21b73f6fbce04b8806b61a
# seed: 2515908707

# Time:  O(n)
# Space: O(1)

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # @param root, a tree node
    # @return root of the upside down tree
    def upsideDownBinaryTree(self, root):
        p, parent, parent_right = root, None, None

        while p:
            left = p.left
            p.left = parent_right
            parent_right = p.right
            p.right = parent
            parent = p
            p = left

        return parent