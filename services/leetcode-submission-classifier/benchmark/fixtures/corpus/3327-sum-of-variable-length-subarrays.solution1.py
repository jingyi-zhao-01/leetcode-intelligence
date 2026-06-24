# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sum-of-variable-length-subarrays
# source_path: LeetCode-Solutions-master/Python/sum-of-variable-length-subarrays.py
# solution_class: Solution
# submission_id: 71156fef6c97209d190f1525a61dc59986f4ee17
# seed: 3620841973

# Time:  O(n)
# Space: O(n)

# difference array

class Solution(object):
    def subarraySum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        diff = [0]*(len(nums)+1)
        for i, x in enumerate(nums):
            diff[max(i-x, 0)] += 1
            diff[i+1] -= 1
        for i in xrange(len(nums)):
            diff[i+1] += diff[i]
        return sum(nums[i]*diff[i] for i in xrange(len(nums)))