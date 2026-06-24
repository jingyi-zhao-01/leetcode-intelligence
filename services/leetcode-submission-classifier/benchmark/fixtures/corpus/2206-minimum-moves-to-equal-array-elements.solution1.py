# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-moves-to-equal-array-elements
# source_path: LeetCode-Solutions-master/Python/minimum-moves-to-equal-array-elements.py
# solution_class: Solution
# submission_id: 7f22c970ed59f19f960fff26c79df8346a6be81b
# seed: 3809030471

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums) - len(nums) * min(nums)