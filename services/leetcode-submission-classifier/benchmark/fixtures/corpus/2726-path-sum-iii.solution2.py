# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: path-sum-iii
# source_path: LeetCode-Solutions-master/Python/path-sum-iii.py
# solution_class: Solution2
# submission_id: fcd09541c4f29d50108163ec53d1433e1724271d
# seed: 362534295

# Time:  O(n)
# Space: O(h)

import collections

class Solution2(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        def pathSumHelper(root, prev, sum):
            if root is None:
                return 0

            curr = prev + root.val
            return int(curr == sum) + \
                   pathSumHelper(root.left, curr, sum) + \
                   pathSumHelper(root.right, curr, sum)

        if root is None:
            return 0

        return pathSumHelper(root, 0, sum) + \
               self.pathSum(root.left, sum) + \
               self.pathSum(root.right, sum)