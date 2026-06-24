# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: max-pair-sum-in-an-array
# source_path: LeetCode-Solutions-master/Python/max-pair-sum-in-an-array.py
# solution_class: Solution
# submission_id: 60827938fa97dd2d71731398d70dfd44eba2c8ed
# seed: 3610044506

# Time:  O(nlogr)
# Space: O(1)

# hash table

class Solution(object):
    def maxSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def max_digit(x):
            result = 0
            while x:
                x, r = divmod(x, 10)
                result = max(result, r)
            return result
    
        result = -1
        lookup = {}
        for x in nums:
            mx = max_digit(x)
            if mx not in lookup:
                lookup[mx] = x
                continue
            result = max(result, lookup[mx]+x)
            lookup[mx] = max(lookup[mx], x)
        return result