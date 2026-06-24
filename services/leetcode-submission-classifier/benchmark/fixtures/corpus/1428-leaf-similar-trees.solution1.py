# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: leaf-similar-trees
# source_path: LeetCode-Solutions-master/Python/leaf-similar-trees.py
# solution_class: Solution
# submission_id: ad59007ba98092f6f8881ae3e8f9b5ccb66a3fdc
# seed: 67594739

# Time:  O(n)
# Space: O(h)

import itertools


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def dfs(node):
            if not node:
                return
            if not node.left and not node.right:
                yield node.val
            for i in dfs(node.left):
                yield i
            for i in dfs(node.right):
                yield i
        return all(a == b for a, b in
                   itertools.izip_longest(dfs(root1), dfs(root2)))