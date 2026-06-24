# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-dominant-indices
# source_path: LeetCode-Solutions-master/Python/count-dominant-indices.py
# solution_class: Solution
# submission_id: 23f46189aadb2fbc9b25aa7c301bf3316caa746a
# seed: 4181691391

# Time:  O(n)
# Space: O(1)

# array

class Solution(object):
    def dominantIndices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = total = 0
        for i in xrange(len(nums)):
            if i*nums[~i] > total:
                result += 1
            total += nums[~i]
        return result