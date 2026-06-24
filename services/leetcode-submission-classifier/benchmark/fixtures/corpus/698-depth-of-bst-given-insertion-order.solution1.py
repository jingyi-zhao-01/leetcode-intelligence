# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: depth-of-bst-given-insertion-order
# source_path: LeetCode-Solutions-master/Python/depth-of-bst-given-insertion-order.py
# solution_class: Solution
# submission_id: e8b6fae44c6307beb7073503d65c5dcfcc7825e9
# seed: 3357211304

# Time:  O(nlogn)
# Space: O(n)

import sortedcontainers

class Solution(object):
    def maxDepthBST(self, order):
        """
        :type order: List[int]
        :rtype: int
        """
        depths = sortedcontainers.SortedDict({float("-inf"):0, float("inf"):0})
        values_view = depths.values()
        result = 0
        for x in order:
            i = depths.bisect_right(x)
            depths[x] = max(values_view[i-1:i+1])+1
            result = max(result, depths[x])
        return result