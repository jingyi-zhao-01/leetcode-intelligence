# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: second-minimum-node-in-a-binary-tree
# source_path: LeetCode-Solutions-master/Python/second-minimum-node-in-a-binary-tree.py
# solution_class: Solution
# submission_id: 67ea284cfd1d85c03e59575b03d25ca415c033ae
# seed: 2106089653

# Time:  O(n)
# Space: O(h)

import heapq

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def findSecondMinimumValueHelper(root, max_heap, lookup):
            if not root:
                return
            if root.val not in lookup:
                heapq.heappush(max_heap, -root.val)
                lookup.add(root.val)
                if len(max_heap) > 2:
                    lookup.remove(-heapq.heappop(max_heap))
            findSecondMinimumValueHelper(root.left, max_heap, lookup)
            findSecondMinimumValueHelper(root.right, max_heap, lookup)

        max_heap, lookup = [], set()
        findSecondMinimumValueHelper(root, max_heap, lookup)
        if len(max_heap) < 2:
            return -1
        return -max_heap[0]