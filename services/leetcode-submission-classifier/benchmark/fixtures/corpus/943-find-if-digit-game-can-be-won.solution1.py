# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-if-digit-game-can-be-won
# source_path: LeetCode-Solutions-master/Python/find-if-digit-game-can-be-won.py
# solution_class: Solution
# submission_id: 7e54413dbc50cdbd49d0ad8770dbf317f5cbdf0d
# seed: 1066368122

# Time:  O(n)
# Space: O(1)

# brute force, game theory

class Solution(object):
    def canAliceWin(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total1 = total2 = 0
        for x in nums:
            if x < 10:
                total1 += x
            else:
                total2 += x
        return total1 != total2