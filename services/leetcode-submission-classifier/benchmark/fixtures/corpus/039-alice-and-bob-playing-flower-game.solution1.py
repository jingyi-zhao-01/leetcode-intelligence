# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: alice-and-bob-playing-flower-game
# source_path: LeetCode-Solutions-master/Python/alice-and-bob-playing-flower-game.py
# solution_class: Solution
# submission_id: 04ae473beb8203fe3c052429b892dc28a8c1de6a
# seed: 1750536023

# Time:  O(1)
# Space: O(1)

# combinatorics

class Solution(object):
    def flowerGame(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        return (n*m)//2