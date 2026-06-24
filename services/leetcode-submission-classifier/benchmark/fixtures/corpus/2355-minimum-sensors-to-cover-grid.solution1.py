# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-sensors-to-cover-grid
# source_path: LeetCode-Solutions-master/Python/minimum-sensors-to-cover-grid.py
# solution_class: Solution
# submission_id: 0ec511a5d0ac83e97ca76873806f479692078fea
# seed: 762198756

# Time:  O(1)
# Space: O(1)

# math

class Solution(object):
    def minSensors(self, n, m, k):
        """
        :type n: int
        :type m: int
        :type k: int
        :rtype: int
        """
        def ceil_divide(a, b):
            return (a+b-1)//b
    
        return ceil_divide(n, 2*k+1)*ceil_divide(m, 2*k+1)