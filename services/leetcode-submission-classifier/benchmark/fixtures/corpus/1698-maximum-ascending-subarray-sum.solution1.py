# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-ascending-subarray-sum
# source_path: LeetCode-Solutions-master/Python/maximum-ascending-subarray-sum.py
# solution_class: Solution
# submission_id: da0be7ce9db7eb617431daa5a033d5a393b85342
# seed: 2377082612

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = curr = 0
        for i in xrange(len(nums)): 
            if not (i and nums[i-1] < nums[i]):
                curr = 0
            curr += nums[i]
            result = max(result, curr)
        return result