# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: pseudo-palindromic-paths-in-a-binary-tree
# source_path: LeetCode-Solutions-master/Python/pseudo-palindromic-paths-in-a-binary-tree.py
# solution_class: Solution
# submission_id: 8ed81b0ae093ef489245e8dd315ec37b098e4225
# seed: 3946852667

# Time:  O(n)
# Space: O(h)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def pseudoPalindromicPaths (self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = 0
        stk = [(root, 0)]
        while stk:
            node, count = stk.pop()
            if not node:
                continue
            count ^= 1 << (node.val-1)
            result += int(node.left == node.right and count&(count-1) == 0)
            stk.append((node.right, count))
            stk.append((node.left, count))
        return result