# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-alternating-subarrays
# source_path: LeetCode-Solutions-master/Python/count-alternating-subarrays.py
# solution_class: Solution
# submission_id: 02ac2e3472cb9fce724f05b5696ce33d0cf1aab0
# seed: 2269967952

# Time:  O(n)
# Space: O(1)

# dp

class Solution(object):
    def countAlternatingSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = curr = 0
        for i in xrange(len(nums)):
            if i-1 >= 0 and nums[i-1] == nums[i]:
                curr = 0
            curr += 1
            result += curr
        return result