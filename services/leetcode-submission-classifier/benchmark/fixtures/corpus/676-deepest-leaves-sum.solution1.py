# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: deepest-leaves-sum
# source_path: LeetCode-Solutions-master/Python/deepest-leaves-sum.py
# solution_class: Solution
# submission_id: 1ff8ad4fb230e7d01cf6408fc6bae70d4a6c69c6
# seed: 2107948084

# Time:  O(n)
# Space: O(w)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        curr = [root]
        while curr:
            prev, curr = curr, [child for p in curr for child in [p.left, p.right] if child]
        return sum(node.val for node in prev)