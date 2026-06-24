# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: divisor-game
# source_path: LeetCode-Solutions-master/Python/divisor-game.py
# solution_class: Solution
# submission_id: 70dfb3f809e74ab1ff85295daa5733220205779e
# seed: 3861361346

# Time:  O(1)
# Space: O(1)

# math

class Solution(object):
    def divisorGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 1. if we get an even, we can choose x = 1
        #    to make the opponent always get an odd
        # 2. if the opponent gets an odd, he can only choose x = 1 or other odds
        #    and we can still get an even
        # 3. at the end, the opponent can only choose x = 1 and we win
        # 4. in summary, we win if only if we get an even and 
        #    keeps even until the opponent loses
        return n % 2 == 0