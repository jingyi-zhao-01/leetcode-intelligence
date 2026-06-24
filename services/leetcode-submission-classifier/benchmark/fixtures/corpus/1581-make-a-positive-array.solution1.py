# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: make-a-positive-array
# source_path: LeetCode-Solutions-master/Python/make-a-positive-array.py
# solution_class: Solution
# submission_id: 2d7272c6c0d53d2b9a4f399a7e0c9e4ea19e5e36
# seed: 113711620

# Time:  O(n)
# Space: O(1)

# prefix sum, greedy

class Solution(object):
    def makeArrayPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MAX_VAL = 10**18
        result = 0
        prev1 = nums[0]+nums[1]
        prev2 = nums[0]
        max_prev3 = 0
        for i in xrange(2, len(nums)):
            prefix = prev1+nums[i]
            if prefix-max_prev3 <= 0:
                prefix = prev1+MAX_VAL
                result += 1
            max_prev3 = max(max_prev3, prev2)
            prev1, prev2 = prefix, prev1
        return result