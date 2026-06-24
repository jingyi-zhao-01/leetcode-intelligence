# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-depth-of-binary-tree
# source_path: LeetCode-Solutions-master/Python/minimum-depth-of-binary-tree.py
# solution_class: Solution
# submission_id: d9cb6b9b54f6ff29b9d71c32cba903931c372b01
# seed: 3499101917

# Time:  O(n)
# Space: O(h), h is height of binary tree

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if root is None:
            return 0

        if root.left and root.right:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        else:
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1