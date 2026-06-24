# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-strictly-increasing-subarrays
# source_path: LeetCode-Solutions-master/Python/count-strictly-increasing-subarrays.py
# solution_class: Solution
# submission_id: 6e1cd6ad3619f5cc46d92f0a3ff1b666223f644b
# seed: 484991032

# Time:  O(n)
# Space: O(1)

# two pointers

class Solution(object):
    def countSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = l = 1
        for i in xrange(1, len(nums)):
            if nums[i-1] >= nums[i]:
                l = 0
            l += 1
            result += l
        return result