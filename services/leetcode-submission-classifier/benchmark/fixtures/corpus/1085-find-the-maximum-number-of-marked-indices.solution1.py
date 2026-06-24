# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-maximum-number-of-marked-indices
# source_path: LeetCode-Solutions-master/Python/find-the-maximum-number-of-marked-indices.py
# solution_class: Solution
# submission_id: 365100e294c0dbfbb57fee67df90607801a8abd6
# seed: 1479205681

# Time:  O(nlogn)
# Space: O(1)

# sort, greedy, two pointers

class Solution(object):
    def maxNumOfMarkedIndices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        left = 0
        for right in xrange((len(nums)+1)//2, len(nums)):
            if nums[right] >= 2*nums[left]:
                left += 1
        return left*2