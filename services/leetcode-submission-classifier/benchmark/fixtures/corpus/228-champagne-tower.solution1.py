# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: champagne-tower
# source_path: LeetCode-Solutions-master/Python/champagne-tower.py
# solution_class: Solution
# submission_id: 2019c21f955d5fe3a6a9b10fbf36366893d11657
# seed: 3488884801

# Time:  O(n^2) = O(1), since n is at most 99
# Space: O(n) = O(1)

class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        result = [poured] + [0] * query_row
        for i in xrange(1, query_row+1):
            for j in reversed(xrange(i+1)):
                result[j] = max(result[j]-1, 0)/2.0 + \
                            max(result[j-1]-1, 0)/2.0
        return min(result[query_glass], 1)