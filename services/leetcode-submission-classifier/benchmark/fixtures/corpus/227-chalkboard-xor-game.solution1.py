# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: chalkboard-xor-game
# source_path: LeetCode-Solutions-master/Python/chalkboard-xor-game.py
# solution_class: Solution
# submission_id: 5c6db98bc625b8771f83d327a2f774220bfeea00
# seed: 388847822

# Time:  O(n)
# Space: O(1)

from operator import xor
from functools import reduce

class Solution(object):
    def xorGame(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return reduce(xor, nums) == 0 or \
            len(nums) % 2 == 0