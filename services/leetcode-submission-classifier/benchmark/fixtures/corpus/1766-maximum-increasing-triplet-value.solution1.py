# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-increasing-triplet-value
# source_path: LeetCode-Solutions-master/Python/maximum-increasing-triplet-value.py
# solution_class: Solution
# submission_id: 051afdddfb7593a8a6f8bd22036f62e355bbe2f2
# seed: 3688265812

# Time:  O(nlogn)
# Space: O(n)

from sortedcontainers import SortedList


# sorted list, prefix sum

class Solution(object):
    def maximumTripletValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = SortedList()
        right = [0]*len(nums)
        for i in reversed(xrange(1, len(nums)-1)):
            right[i] = max(right[i+1], nums[i+1])
        result = 0
        for i in xrange(1, len(nums)-1):
            left.add(nums[i-1])
            j = left.bisect_left(nums[i])
            if j-1 >= 0 and right[i] > nums[i]:
                result = max(result, left[j-1]-nums[i]+right[i])
        return result