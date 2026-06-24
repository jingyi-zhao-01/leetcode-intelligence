# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-knight-moves
# source_path: LeetCode-Solutions-master/Python/minimum-knight-moves.py
# solution_class: Solution2
# submission_id: 9afa7e38161a473a0e1b0c175529a43eb8eb8bcd
# seed: 673190303

# Time:  O(1)
# Space: O(1)

class Solution2(object):
    def __init__(self):
        self.__lookup = {(0, 0):0, (1, 1):2, (1, 0):3}  # special cases

    def minKnightMoves(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        def dp(x, y):
            x, y = abs(x), abs(y)
            if x < y:
                x, y = y, x
            if (x, y) not in self.__lookup:  # greedy, smaller x, y is always better if not special cases
                self.__lookup[(x, y)] = min(dp(x-1, y-2), dp(x-2, y-1)) + 1
            return self.__lookup[(x, y)]
        return dp(x, y)