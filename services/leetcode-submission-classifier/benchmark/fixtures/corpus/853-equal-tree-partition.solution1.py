# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: equal-tree-partition
# source_path: LeetCode-Solutions-master/Python/equal-tree-partition.py
# solution_class: Solution
# submission_id: 52e1a44da6032dacd4b8baa20c791e69fc6077f5
# seed: 2077670480

# Time:  O(n)
# Space: O(n)

import collections

class Solution(object):
    def checkEqualTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def getSumHelper(node, lookup):
            if not node:
                return 0
            total = node.val + \
                    getSumHelper(node.left, lookup) + \
                    getSumHelper(node.right, lookup)
            lookup[total] += 1
            return total

        lookup = collections.defaultdict(int)
        total = getSumHelper(root, lookup)
        if total == 0:
            return lookup[total] > 1
        return total%2 == 0 and (total/2) in lookup