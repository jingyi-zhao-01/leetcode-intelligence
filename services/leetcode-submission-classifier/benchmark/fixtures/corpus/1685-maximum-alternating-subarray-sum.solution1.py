# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-alternating-subarray-sum
# source_path: LeetCode-Solutions-master/Python/maximum-alternating-subarray-sum.py
# solution_class: Solution
# submission_id: 61a6cae4833b44a679b360b31733543b9127891d
# seed: 2053832520

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def maximumAlternatingSubarraySum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def kadane(nums, start):
            result = float("-inf")
            curr = odd = 0
            for i in xrange(start, len(nums)):
                curr = (curr+nums[i]) if not odd else max(curr-nums[i], 0)
                result = max(result, curr)
                odd ^= 1
            return result

        return max(kadane(nums, 0), kadane(nums, 1))