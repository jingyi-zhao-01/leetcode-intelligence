# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: path-sum
# source_path: LeetCode-Solutions-master/Python/path-sum.py
# solution_class: Solution
# submission_id: 8ba8530fa6b0f49f23eeaba6a99e728b31b11fff
# seed: 1779952423

# Time:  O(n)
# Space: O(h), h is height of binary tree

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if root is None:
            return False

        if root.left is None and root.right is None and root.val == sum:
            return True

        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)