# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-depth-of-binary-tree
# source_path: LeetCode-Solutions-master/Python/maximum-depth-of-binary-tree.py
# solution_class: Solution
# submission_id: bba567101c86813f39495bee229a31256ac3b7a5
# seed: 3928666966

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
    def maxDepth(self, root):
        if root is None:
            return 0
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1