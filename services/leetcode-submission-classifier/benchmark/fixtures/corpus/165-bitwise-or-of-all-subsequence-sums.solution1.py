# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: bitwise-or-of-all-subsequence-sums
# source_path: LeetCode-Solutions-master/Python/bitwise-or-of-all-subsequence-sums.py
# solution_class: Solution
# submission_id: 9e35acc75e929382917fa2ce836bee05c1e4be10
# seed: 345861239

# Time:  O(n)
# Space: O(1)

# bit manipulation

class Solution(object):
    def subsequenceSumOr(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = prefix = 0
        for x in nums:
            prefix += x
            result |= x|prefix
        return result