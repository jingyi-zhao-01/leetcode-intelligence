# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: smallest-index-with-digit-sum-equal-to-index
# source_path: LeetCode-Solutions-master/Python/smallest-index-with-digit-sum-equal-to-index.py
# solution_class: Solution
# submission_id: b679c1f8109681a3c00d4de0ef9c6e5e1bf88f87
# seed: 284573624

# Time:  O(nlogr)
# Space: O(1)

# array

class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def total(x):
            result = 0
            while x:
                result += x%10
                x //= 10
            return result

        return next((i for i, x in enumerate(nums) if total(x) == i), -1)