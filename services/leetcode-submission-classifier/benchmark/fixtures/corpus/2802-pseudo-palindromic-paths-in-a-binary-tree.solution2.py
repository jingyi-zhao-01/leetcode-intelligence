# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: pseudo-palindromic-paths-in-a-binary-tree
# source_path: LeetCode-Solutions-master/Python/pseudo-palindromic-paths-in-a-binary-tree.py
# solution_class: Solution2
# submission_id: e7503de49464022b74ae8d0ecf2a920b0d3a53db
# seed: 733702736

# Time:  O(n)
# Space: O(h)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution2(object):
    def pseudoPalindromicPaths (self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, count):
            if not root:
                return 0
            count ^= 1 << (node.val-1)
            return int(node.left == node.right and count&(count-1) == 0) + \
                   dfs(node.left, count) + dfs(node.right, count)
        return dfs(root, 0)