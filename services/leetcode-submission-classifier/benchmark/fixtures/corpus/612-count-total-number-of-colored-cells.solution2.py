# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-total-number-of-colored-cells
# source_path: LeetCode-Solutions-master/Python/count-total-number-of-colored-cells.py
# solution_class: Solution2
# submission_id: 759a51236b5f1bc553e5e4384c8e802fc68ae239
# seed: 3369774830

# Time:  O(1)
# Space: O(1)

# math

class Solution2(object):
    def coloredCells(self, n):
        """
        :type n: int
        :rtype: int
        """
        return (1+(1+2*(n-1)))*n//2*2-(2*n-1)