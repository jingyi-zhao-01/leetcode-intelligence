# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: nim-game
# source_path: LeetCode-Solutions-master/Python/nim-game.py
# solution_class: Solution
# submission_id: 03b5481f9544af41cb48ed511d381a54c55e1ab9
# seed: 84574379

# Time:  O(1)
# Space: O(1)

class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n % 4 != 0