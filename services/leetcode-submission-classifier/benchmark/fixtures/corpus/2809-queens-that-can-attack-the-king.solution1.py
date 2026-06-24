# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: queens-that-can-attack-the-king
# source_path: LeetCode-Solutions-master/Python/queens-that-can-attack-the-king.py
# solution_class: Solution
# submission_id: d6516645ead17e5bd251944fbe2063a94eba8da6
# seed: 3187778326

# Time:  O(1)
# Space: O(1)

class Solution(object):
    def queensAttacktheKing(self, queens, king):
        """
        :type queens: List[List[int]]
        :type king: List[int]
        :rtype: List[List[int]]
        """
        dirctions = [(-1, 0), (0, 1), (1, 0), (0, -1),
                     (-1, 1), (1, 1), (1, -1), (-1, -1)]
        result = []
        lookup = {(i, j) for i, j in queens}
        for dx, dy in dirctions:
            for i in xrange(1, 8):
                x, y = king[0] + dx*i, king[1] + dy*i
                if (x, y) in lookup:
                    result.append([x, y])
                    break
        return result