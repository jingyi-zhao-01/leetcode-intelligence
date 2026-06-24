# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: game-of-nim
# source_path: LeetCode-Solutions-master/Python/game-of-nim.py
# solution_class: Solution
# submission_id: 6091ff888c9b7f4bd505c6ef98fa3beef0a21c0d
# seed: 2850679894

# Time:  O(n)
# Space: O(1)

import operator

class Solution(object):
    def nimGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        return reduce(operator.xor, piles, 0)