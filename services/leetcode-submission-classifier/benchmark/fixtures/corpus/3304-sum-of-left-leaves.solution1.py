# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sum-of-left-leaves
# source_path: LeetCode-Solutions-master/Python/sum-of-left-leaves.py
# solution_class: Solution
# submission_id: 2e043f4458c5ad4a57ce3dd359421506d7de6a75
# seed: 1472053191

# Time:  O(n)
# Space: O(h)

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def sumOfLeftLeavesHelper(root, is_left):
            if not root:
                return 0
            if not root.left and not root.right:
                return root.val if is_left else 0
            return sumOfLeftLeavesHelper(root.left, True) + \
                   sumOfLeftLeavesHelper(root.right, False)

        return sumOfLeftLeavesHelper(root, False)