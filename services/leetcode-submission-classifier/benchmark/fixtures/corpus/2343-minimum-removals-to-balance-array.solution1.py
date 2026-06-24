# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-removals-to-balance-array
# source_path: LeetCode-Solutions-master/Python/minimum-removals-to-balance-array.py
# solution_class: Solution
# submission_id: e7992fed6641fae7588fef741b0eae73b059e1a9
# seed: 4249626507

# Time:  O(nlogn)
# Space: O(1)

# sort, two pointers

class Solution(object):
    def minRemoval(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        left = 0
        for right in xrange(len(nums)):
            if nums[left]*k < nums[right]:
                left += 1
        return left