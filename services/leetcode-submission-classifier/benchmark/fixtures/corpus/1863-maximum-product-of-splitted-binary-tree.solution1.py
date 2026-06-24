# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-product-of-splitted-binary-tree
# source_path: LeetCode-Solutions-master/Python/maximum-product-of-splitted-binary-tree.py
# solution_class: Solution
# submission_id: 10be59d997c6681dc1697e164699ea5ef562cde3
# seed: 4045431851

# Time:  O(n)
# Space: O(h)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxProduct(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        MOD = 10**9 + 7
        def dfs(root, total, result):
            if not root:
                return 0
            subtotal = dfs(root.left, total, result)+dfs(root.right, total, result)+root.val
            result[0] = max(result[0], subtotal*(total-subtotal) )
            return subtotal

        result = [0]
        dfs(root, dfs(root, 0, result), result)
        return result[0] % MOD