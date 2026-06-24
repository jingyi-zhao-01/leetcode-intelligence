# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-winning-player-in-coin-game
# source_path: LeetCode-Solutions-master/Python/find-the-winning-player-in-coin-game.py
# solution_class: Solution
# submission_id: 3b5eb0145ec13558dfe186d976a7792d20f8e344
# seed: 3989160966

# Time:  O(1)
# Space: O(1)

# math

class Solution(object):
    def losingPlayer(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: str
        """
        return "Alice" if min(x, y//4)%2 else "Bob"