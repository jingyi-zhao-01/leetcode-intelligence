# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-pairs-satisfying-inequality
# source_path: LeetCode-Solutions-master/Python/number-of-pairs-satisfying-inequality.py
# solution_class: Solution2
# submission_id: aac854b435c897af458f70bd72cc61142acbb7be
# seed: 2440011484

# Time:  O(nlogn)
# Space: O(n)

from sortedcontainers import SortedList
import itertools


# sorted list, binary search

class Solution2(object):
    def numberOfPairs(self, nums1, nums2, diff):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type diff: int
        :rtype: int
        """
        sorted_nums = sorted(set(x-y for x, y in itertools.izip(nums1, nums2)))
        num_to_idx = {x:i for i, x in enumerate(sorted_nums)}
        result = 0
        bit = BIT(len(num_to_idx))
        for x, y in itertools.izip(nums1, nums2):
            result += bit.query(bisect.bisect_right(sorted_nums, (x-y)+diff)-1)
            bit.add(num_to_idx[x-y], 1)
        return result