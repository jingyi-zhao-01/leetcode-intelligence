# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: house-robber-iii
# source_path: LeetCode-Solutions-master/Python/house-robber-iii.py
# solution_class: Solution
# submission_id: 6db017945ebff5e7d6338d8dc33fdd2c48c9b462
# seed: 2337121231

# Time:  O(n)
# Space: O(h)

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def robHelper(root):
            if not root:
                return (0, 0)
            left, right = robHelper(root.left), robHelper(root.right)
            return (root.val + left[1] + right[1], max(left) + max(right))

        return max(robHelper(root))