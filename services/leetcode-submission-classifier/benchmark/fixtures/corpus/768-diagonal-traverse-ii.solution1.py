# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: diagonal-traverse-ii
# source_path: LeetCode-Solutions-master/Python/diagonal-traverse-ii.py
# solution_class: Solution
# submission_id: 3c4c611218cf02135a46d601ac14276ea80e834a
# seed: 1913809150

# Time:  O(m * n)
# Space: O(m)

import itertools
import collections

class Solution(object):
    def findDiagonalOrder(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        result, dq, col = [], collections.deque(), 0
        for i in xrange(len(nums)+max(itertools.imap(len, nums))-1):
            new_dq = collections.deque()
            if i < len(nums):
                dq.appendleft((i, 0))
            for r, c in dq:
                result.append(nums[r][c])
                if c+1 < len(nums[r]):
                    new_dq.append((r, c+1))
            dq = new_dq
        return result