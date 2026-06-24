# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-total-number-of-colored-cells
# source_path: LeetCode-Solutions-master/Python/count-total-number-of-colored-cells.py
# solution_class: Solution
# submission_id: 858776ede9fae3b4b2be1365365851b5776ebe7f
# seed: 4183954013

# Time:  O(1)
# Space: O(1)

# math

class Solution(object):
    def coloredCells(self, n):
        """
        :type n: int
        :rtype: int
        """
        return n**2+(n-1)**2