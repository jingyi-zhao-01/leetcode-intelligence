# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: root-equals-sum-of-children
# source_path: LeetCode-Solutions-master/Python/root-equals-sum-of-children.py
# solution_class: Solution
# submission_id: 389e2972d1d5d0ed15a94f8caa355143bd6ee812
# seed: 3967867782

# Time:  O(1)
# Space: O(1)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        pass


# tree

class Solution(object):
    def checkTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return root.val == root.left.val+root.right.val