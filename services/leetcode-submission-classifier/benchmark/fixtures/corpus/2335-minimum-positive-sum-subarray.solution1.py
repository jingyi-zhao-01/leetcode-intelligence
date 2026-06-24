# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-positive-sum-subarray
# source_path: LeetCode-Solutions-master/Python/minimum-positive-sum-subarray.py
# solution_class: Solution
# submission_id: e0cd523528d8e162ae0c4197266ce1b33e3d7fb9
# seed: 2352919662

# Time:  O(nlogn)
# Space: O(n)

from sortedcontainers import SortedList


# prefix sum, two pointers, sliding window, sorted list, binary search

class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: int
        :type r: int
        :rtype: int
        """
        INF = float("inf")
        prefix = [0]*(len(nums)+1)
        for i in xrange(len(nums)):
            prefix[i+1] = prefix[i]+nums[i]
        result = INF
        sl = SortedList()
        for i in xrange(len(nums)):
            if i-l+1 >= 0:
                sl.add(prefix[i-l+1])
            if i-r >= 0:
                sl.remove(prefix[i-r])
            idx = sl.bisect_left(prefix[i+1])-1
            if idx >= 0:
                result = min(result, prefix[i+1]-sl[idx])
        return result if result != INF else -1