# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: validate-binary-search-tree
# source_path: LeetCode-Solutions-master/Python/validate-binary-search-tree.py
# solution_class: Solution2
# submission_id: 2626b7f6b15a561c72fb3c5f77c4df9908889d9f
# seed: 1224482401

# Time:  O(n)
# Space: O(1)

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Morris Traversal Solution

class Solution2(object):
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        return self.isValidBSTRecu(root, float("-inf"), float("inf"))

    def isValidBSTRecu(self, root, low, high):
        if root is None:
            return True

        return low < root.val and root.val < high \
            and self.isValidBSTRecu(root.left, low, root.val) \
            and self.isValidBSTRecu(root.right, root.val, high)