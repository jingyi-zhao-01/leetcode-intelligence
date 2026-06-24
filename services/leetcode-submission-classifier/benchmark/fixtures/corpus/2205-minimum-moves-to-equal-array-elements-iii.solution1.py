# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-moves-to-equal-array-elements-iii
# source_path: LeetCode-Solutions-master/Python/minimum-moves-to-equal-array-elements-iii.py
# solution_class: Solution
# submission_id: 663684e1843560b6f0167165a8fb9ec8a0569460
# seed: 565298344

# Time:  O(n)
# Space: O(1)

# array

class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return max(nums)*len(nums)-sum(nums)