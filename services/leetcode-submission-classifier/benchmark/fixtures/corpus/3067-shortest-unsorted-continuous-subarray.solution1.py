# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: shortest-unsorted-continuous-subarray
# source_path: LeetCode-Solutions-master/Python/shortest-unsorted-continuous-subarray.py
# solution_class: Solution
# submission_id: 281e1553380693fae97e6ef519d61dc2cb406e14
# seed: 4229476927

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        left, right = -1, -2
        min_from_right, max_from_left = nums[-1], nums[0]
        for i in xrange(1, n):
            max_from_left = max(max_from_left, nums[i])
            min_from_right = min(min_from_right, nums[n-1-i])
            if nums[i] < max_from_left: right = i
            if nums[n-1-i] > min_from_right: left = n-1-i