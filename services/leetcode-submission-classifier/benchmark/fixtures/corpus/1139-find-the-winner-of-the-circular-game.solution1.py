# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-winner-of-the-circular-game
# source_path: LeetCode-Solutions-master/Python/find-the-winner-of-the-circular-game.py
# solution_class: Solution
# submission_id: d98db6011c596b829ba3bddbe7bb72fcfd9f38ea
# seed: 613180693

# Time:  O(n)
# Space: O(1)

# bottom-up solution

class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        return reduce(lambda idx, n:(idx+k)%(n+1), xrange(1, n), 0)+1