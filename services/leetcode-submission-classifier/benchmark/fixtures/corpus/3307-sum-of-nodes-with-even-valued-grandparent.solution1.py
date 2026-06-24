# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sum-of-nodes-with-even-valued-grandparent
# source_path: LeetCode-Solutions-master/Python/sum-of-nodes-with-even-valued-grandparent.py
# solution_class: Solution
# submission_id: b488ec4f5d5bf7d1f275bac4eb7968ca8d47772d
# seed: 812165345

# Time:  O(n)
# Space: O(h)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def sumEvenGrandparentHelper(root, p, gp):
            return sumEvenGrandparentHelper(root.left, root.val, p) + \
                   sumEvenGrandparentHelper(root.right, root.val, p) + \
                   (root.val if gp is not None and gp % 2 == 0 else 0) if root else 0

        return sumEvenGrandparentHelper(root, None, None)