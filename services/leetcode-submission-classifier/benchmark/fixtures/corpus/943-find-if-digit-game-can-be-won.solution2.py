# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-if-digit-game-can-be-won
# source_path: LeetCode-Solutions-master/Python/find-if-digit-game-can-be-won.py
# solution_class: Solution2
# submission_id: c7dd74bc4df9c65a03059469bcf6a991485b2b7a
# seed: 4099154368

# Time:  O(n)
# Space: O(1)

# brute force, game theory

class Solution2(object):
    def canAliceWin(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return sum(x for x in nums if x < 10) != sum(x for x in nums if x >= 10)