# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: binary-tree-vertical-order-traversal
# source_path: LeetCode-Solutions-master/Python/binary-tree-vertical-order-traversal.py
# solution_class: Solution
# submission_id: 400ea01bbcbf2e184ca43ecd92f2e04db66ae019
# seed: 823267149

# Time:  O(n)
# Space: O(n)

import collections


# BFS + hash solution.

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        cols = collections.defaultdict(list)
        queue = [(root, 0)]
        for node, i in queue:
            if node:
                cols[i].append(node.val)
                queue += (node.left, i - 1), (node.right, i + 1)
        return [cols[i] for i in xrange(min(cols.keys()),
                                        max(cols.keys()) + 1)] if cols else []