# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: distribute-coins-in-binary-tree
# source_path: LeetCode-Solutions-master/Python/distribute-coins-in-binary-tree.py
# solution_class: Solution
# submission_id: 4eb4a17c9ddbf6d0644e679922fa3161f4337e1f
# seed: 3572559839

# Time:  O(n)
# Space: O(h)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

        

class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root, result):
            if not root:
                return 0
            left, right = dfs(root.left, result), dfs(root.right, result)
            result[0] += abs(left) + abs(right)
            return root.val + left + right - 1

        result = [0]
        dfs(root, result)
        return result[0]