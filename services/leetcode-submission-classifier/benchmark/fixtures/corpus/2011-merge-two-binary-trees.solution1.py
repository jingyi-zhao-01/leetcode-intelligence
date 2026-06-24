# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: merge-two-binary-trees
# source_path: LeetCode-Solutions-master/Python/merge-two-binary-trees.py
# solution_class: Solution
# submission_id: fe276229aa01a71f1985a41ff7037cdf2cc6c645
# seed: 1465402068

# Time:  O(n)
# Space: O(h)

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 is None:
            return t2
        if t2 is None:
            return t1
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1