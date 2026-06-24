# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-operations-to-make-binary-array-elements-equal-to-one-ii
# source_path: LeetCode-Solutions-master/Python/minimum-operations-to-make-binary-array-elements-equal-to-one-ii.py
# solution_class: Solution
# submission_id: d8344729eb9ff0d54c4d39e65c55e60eb4376e6f
# seed: 1541474904

# Time:  O(n)
# Space: O(1)

# greedy

class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for x in nums:
            if x^(result&1):
                continue
            result += 1
        return result