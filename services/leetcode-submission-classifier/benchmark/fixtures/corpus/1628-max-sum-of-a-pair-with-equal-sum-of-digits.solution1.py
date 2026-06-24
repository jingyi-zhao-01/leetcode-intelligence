# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: max-sum-of-a-pair-with-equal-sum-of-digits
# source_path: LeetCode-Solutions-master/Python/max-sum-of-a-pair-with-equal-sum-of-digits.py
# solution_class: Solution
# submission_id: b0c3845ece250924b6c1aa9862f4c32f0f01f335
# seed: 3644934739

# Time:  O(nlogr), r is max(nums)
# Space: O(n)

# greedy

class Solution(object):
    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def sum_digits(x):
            result = 0
            while x:
                result += x%10
                x //= 10
            return result

        lookup = {}
        result = -1
        for x in nums:
            k = sum_digits(x)
            if k not in lookup:
                lookup[k] = x
                continue
            result = max(result, lookup[k]+x)
            if x > lookup[k]:
                lookup[k] = x
        return result