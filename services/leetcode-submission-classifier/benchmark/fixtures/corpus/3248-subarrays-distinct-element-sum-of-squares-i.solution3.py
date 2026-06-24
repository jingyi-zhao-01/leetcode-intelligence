# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: subarrays-distinct-element-sum-of-squares-i
# source_path: LeetCode-Solutions-master/Python/subarrays-distinct-element-sum-of-squares-i.py
# solution_class: Solution3
# submission_id: e2e55b913cdc930b06568db1dc180e89481ef2ca
# seed: 351227309

# Time:  O(nlogn)
# Space: O(n)

import collections
from sortedcontainers import SortedList


# bit, fenwick tree, sorted list, math

class Solution3(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9+7
        result = 0
        for i in xrange(len(nums)):
            lookup = set()
            for j in reversed(xrange(i+1)):
                lookup.add(nums[j])
                result = (result+len(lookup)**2) % MOD
        return result