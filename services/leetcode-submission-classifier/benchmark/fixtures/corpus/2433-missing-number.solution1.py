# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: missing-number
# source_path: LeetCode-Solutions-master/Python/missing-number.py
# solution_class: Solution
# submission_id: 63b61d6a048971c1d0d803deaf7b3657a05a0fb6
# seed: 2994154948

# Time:  O(n)
# Space: O(1)

import operator

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(operator.xor, nums,
                      reduce(operator.xor, xrange(len(nums) + 1)))