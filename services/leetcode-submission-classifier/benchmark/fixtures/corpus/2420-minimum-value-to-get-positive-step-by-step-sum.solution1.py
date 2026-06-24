# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-value-to-get-positive-step-by-step-sum
# source_path: LeetCode-Solutions-master/Python/minimum-value-to-get-positive-step-by-step-sum.py
# solution_class: Solution
# submission_id: a9f2511834176f1dfdb35f1a6ab2f7e6f2f8183d
# seed: 3906635477

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_prefix, prefix = 0, 0
        for num in nums:
            prefix += num
            min_prefix = min(min_prefix, prefix)
        return 1-min_prefix