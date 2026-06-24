# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sum-of-weighted-modes-in-subarrays
# source_path: LeetCode-Solutions-master/Python/sum-of-weighted-modes-in-subarrays.py
# solution_class: Solution
# submission_id: ab728d55eae64453e1cc61c8d393d00cf030d1c7
# seed: 1770174984

# Time:  O(nlogk)
# Space: O(k)

import collections
from sortedcontainers import SortedList


# sorted list, two pointers, sliding window

class Solution(object):
    def modeWeight(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def add(x, diff):
            if cnt[x]:
                sl.remove((-cnt[x], x))
            cnt[x] += diff
            if cnt[x]:
                sl.add((-cnt[x], x))
            else:
                del cnt[x]
    
        cnt = collections.defaultdict(int)
        sl = SortedList()
        result = 0
        for i in xrange(len(nums)):
            add(nums[i], +1)
            if i >= k-1:
                result += -sl[0][0]*sl[0][1]
                add(nums[i-k+1], -1)
        return result