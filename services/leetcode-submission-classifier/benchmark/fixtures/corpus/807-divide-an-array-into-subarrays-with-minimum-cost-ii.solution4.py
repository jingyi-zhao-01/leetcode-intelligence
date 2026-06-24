# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: divide-an-array-into-subarrays-with-minimum-cost-ii
# source_path: LeetCode-Solutions-master/Python/divide-an-array-into-subarrays-with-minimum-cost-ii.py
# solution_class: Solution4
# submission_id: 7a01ef941e8376130402e14294ea37e1dff664e1
# seed: 765748389

# Time:  O(nlogd)
# Space: O(d)

import heapq


# sliding window, heap

class Solution4(object):
    def minimumCost(self, nums, k, dist):
        """
        :type nums: List[int]
        :type k: int
        :type dist: int
        :rtype: int
        """
        sl = SortedList(nums[1:1+(1+dist)])
        mn = curr = sum(sl[:k-1])
        for i in xrange(1+(1+dist), len(nums)):
            sl.add(nums[i])
            curr += min(nums[i]-sl[k-1], 0)
            curr -= min(nums[i-(1+dist)]-sl[k-1], 0)
            sl.remove(nums[i-(1+dist)])
            mn = min(mn, curr)
        return nums[0]+mn