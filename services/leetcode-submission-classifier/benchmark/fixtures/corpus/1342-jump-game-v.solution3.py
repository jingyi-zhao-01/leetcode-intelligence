# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: jump-game-v
# source_path: LeetCode-Solutions-master/Python/jump-game-v.py
# solution_class: Solution3
# submission_id: 2d8f5aab215ba9eb0dff479f724620a5e754cbf9
# seed: 3756629215

# Time:  O(n)
# Space: O(n)

import collections
import itertools


# sliding window + top-down dp

class Solution3(object):
    def maxJumps(self, arr, d):
        """
        :type arr: List[int]
        :type d: int
        :rtype: int
        """
        left, decreasing_stk = range(len(arr)), []
        for i in xrange(len(arr)):
            while decreasing_stk and arr[decreasing_stk[-1]] < arr[i]:
                if i - decreasing_stk[-1] <= d:
                    left[i] = decreasing_stk[-1]
                decreasing_stk.pop()
            decreasing_stk.append(i)
        right, decreasing_stk = range(len(arr)), []
        for i in reversed(xrange(len(arr))):
            while decreasing_stk and arr[decreasing_stk[-1]] < arr[i]:
                if decreasing_stk[-1] - i <= d:
                    right[i] = decreasing_stk[-1]
                decreasing_stk.pop()
            decreasing_stk.append(i)

        segment_tree = SegmentTree(len(arr))
        for _, i in sorted([x, i] for i, x in enumerate(arr)):
            segment_tree.update(i, i, segment_tree.query(left[i], right[i]) + 1)
        return segment_tree.query(0, len(arr)-1)