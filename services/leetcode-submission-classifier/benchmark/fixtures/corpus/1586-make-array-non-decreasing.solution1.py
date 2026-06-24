# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: make-array-non-decreasing
# source_path: LeetCode-Solutions-master/Python/make-array-non-decreasing.py
# solution_class: Solution
# submission_id: be35c30876b91cf8fb9b36ca44df17714b7ae623
# seed: 982170187

# Time:  O(n)
# Space: O(1)

# greedy

class Solution(object):
    def maximumPossibleSize(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = prev = 0
        for x in nums:
            if prev <= x:
                prev = x
                result += 1
        return result