# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-increasing-triplet-value
# source_path: LeetCode-Solutions-master/Python/maximum-increasing-triplet-value.py
# solution_class: Solution2
# submission_id: 446b18152918669b7e9a52bcfe36c3ae2240fc72
# seed: 1905186722

# Time:  O(nlogn)
# Space: O(n)

from sortedcontainers import SortedList


# sorted list, prefix sum

class Solution2(object):
    def maximumTripletValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = SortedList()
        right = SortedList(nums[i] for i in xrange(1, len(nums)))
        result = 0
        for i in xrange(1, len(nums)-1):
            left.add(nums[i-1])
            right.remove(nums[i])
            j = left.bisect_left(nums[i])
            if j-1 >= 0 and right[-1] > nums[i]:
                result = max(result, left[j-1]-nums[i]+right[-1])
        return result