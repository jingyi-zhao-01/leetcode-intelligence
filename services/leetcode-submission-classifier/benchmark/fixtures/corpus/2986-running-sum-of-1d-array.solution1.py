# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: running-sum-of-1d-array
# source_path: LeetCode-Solutions-master/Python/running-sum-of-1d-array.py
# solution_class: Solution
# submission_id: 8a1018f82f0ca1f48c5e7d71fa7b14420dad5bf1
# seed: 2661572703

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in xrange(len(nums)-1):
            nums[i+1] += nums[i]
        return nums