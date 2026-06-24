# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: divide-an-array-into-subarrays-with-minimum-cost-ii
# source_path: LeetCode-Solutions-master/Python/divide-an-array-into-subarrays-with-minimum-cost-ii.py
# solution_class: Solution3
# submission_id: 44592536e224e934e1295d4ce01c3abae89bb0e0
# seed: 2995888691

# Time:  O(nlogd)
# Space: O(d)

import heapq


# sliding window, heap

class Solution3(object):
    def minimumCost(self, nums, k, dist):
        """
        :type nums: List[int]
        :type k: int
        :type dist: int
        :rtype: int
        """
        sl1, sl2 = SortedList(), SortedList()
        mn, curr = float("inf"), 0
        for i in xrange(1, len(nums)):
            sl1.add(nums[i])
            curr += nums[i]
            if len(sl1) > k-1:
                curr -= sl1[-1]
                sl2.add(sl1.pop())
            if len(sl1)+len(sl2) > 1+dist:
                if sl2[0] <= nums[i-(1+dist)]:
                    sl2.remove(nums[i-(1+dist)])
                else:
                    sl1.remove(nums[i-(1+dist)])
                    curr -= nums[i-(1+dist)]-sl2[0]
                    sl1.add(sl2.pop(0))
            if len(sl1) == k-1:
                mn = min(mn, curr)
        return nums[0]+mn