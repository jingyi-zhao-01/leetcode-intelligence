# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sum-of-good-numbers
# source_path: LeetCode-Solutions-master/Python/sum-of-good-numbers.py
# solution_class: Solution
# submission_id: 6615161ea3456b12247201132043c7fe7c791858
# seed: 4138780567

# Time:  O(n)
# Space: O(1)

# array

class Solution(object):
    def sumOfGoodNumbers(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return sum(nums[i] for i in xrange(len(nums)) if (i-k < 0 or nums[i-k] < nums[i]) and (i+k >= len(nums) or nums[i+k] < nums[i]))