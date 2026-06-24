# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-level-sum-of-a-binary-tree
# source_path: LeetCode-Solutions-master/Python/maximum-level-sum-of-a-binary-tree.py
# solution_class: Solution
# submission_id: 28ecec0587098eff824c684b8d76587c46904ab7
# seed: 3682717426

# Time:  O(n)
# Space: O(h)

import collections


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# dfs solution

class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, i, level_sums):
            if not node:
                return
            if i == len(level_sums):
                level_sums.append(0)
            level_sums[i] += node.val
            dfs(node.left, i+1, level_sums)
            dfs(node.right, i+1, level_sums)

        level_sums = []
        dfs(root, 0, level_sums)
        return level_sums.index(max(level_sums))+1