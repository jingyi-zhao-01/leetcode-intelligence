# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-cost-homecoming-of-a-robot-in-a-grid
# source_path: LeetCode-Solutions-master/Python/minimum-cost-homecoming-of-a-robot-in-a-grid.py
# solution_class: Solution
# submission_id: 39f1f780f4db401b41df6b80c307ad100d45eafa
# seed: 150587003

# Time:  O(m + n)
# Space: O(1)

class Solution(object):
    def minCost(self, startPos, homePos, rowCosts, colCosts):
        """
        :type startPos: List[int]
        :type homePos: List[int]
        :type rowCosts: List[int]
        :type colCosts: List[int]
        :rtype: int
        """
        [x0, y0], [x1, y1] = startPos, homePos
        return (sum(rowCosts[i] for i in xrange(min(x0, x1), max(x0, x1)+1))-rowCosts[x0]) + \
               (sum(colCosts[i] for i in xrange(min(y0, y1), max(y0, y1)+1))-colCosts[y0])