# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-knight-moves
# source_path: LeetCode-Solutions-master/Python/minimum-knight-moves.py
# solution_class: Solution
# submission_id: 4f740c9bb6b6511e5761b20b5f7b347d5f17ce30
# seed: 3949861518

# Time:  O(1)
# Space: O(1)

class Solution(object):
    def minKnightMoves(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # we can observe from:
        # [0]
        # [3, 2]
        # [2,(1),4]
        # [3, 2, 3, 2]
        # [2, 3,(2) 3, 4]
        # [3, 4, 3, 4, 3, 4]
        # [4, 3, 4,(3),4, 5, 4]
        # [5, 4, 5, 4, 5, 4, 5, 6]
        # [4, 5, 4, 5,(4),5, 6, 5, 6]
        # [5, 6, 5, 6, 5, 6, 5, 6, 7, 6]
        # [6, 5, 6, 5, 6,(5),6, 7, 6, 7, 8]
        # [7, 6, 7, 6, 7, 6, 7, 6, 7, 8, 7, 8]
        # [6, 7, 6, 7, 6, 7,(6),7, 8, 7, 8, 9, 8]
        # [7, 8, 7, 8, 7, 8, 7, 8, 7, 8, 9, 8, 9, 10]
        # [8, 7, 8, 7, 8, 7, 8,(7),8, 9, 8, 9, 10, 9, 10]
        # [9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 10, 9, 10, 11, 10]

        x, y = abs(x), abs(y)
        if x < y:
            x, y = y, x
        lookup = {(1, 0):3, (2, 2):4}  # special cases
        if (x, y) in lookup:
            return lookup[(x, y)]
        k = x-y
        if y > k:
            # if 2y > x, every period 3 of y (or k) with fixed another is increased by 2 (or 1)
            # and start from (2k, k) with (k) when y = k (diagonal line)
            # ex. (0, 0) ~ (12, 12) ~ ... : 0 => 2,4(special case),2 => 4,4,4 => 6,6,6 => 8,8,8 => ...
            # ex. (2, 1) ~ (14, 13) ~ ... : 1 => 3,3,3 => 5,5,5 => 7,7,7 => 9,9,9 => ...
            return k - 2*((k-y)//3)
        # if 2y <= x, every period 4 of k (or y) with fixed another is increased by 2
        # and start from (2k, k) with (k) when y = k (vertical line)
        # ex. (0, 0) ~ (11, 0) ~ ... : 0,3(special case),2,3 => 2,3,4,5 => 4,5,6,7 => ...
        # ex. (2, 1) ~ (13, 1) ~ ... : 1,2,3,4 => 3,4,5,6 => 5,6,7,8 => ...
        return k - 2*((k-y)//4)