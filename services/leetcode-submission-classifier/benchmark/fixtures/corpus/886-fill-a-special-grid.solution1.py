# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: fill-a-special-grid
# source_path: LeetCode-Solutions-master/Python/fill-a-special-grid.py
# solution_class: Solution
# submission_id: 6e784a936898de4e703e0c19e196bc4c22982cff
# seed: 3960787198

# Time:  O(4^n)
# Space: O(1)

# array

class Solution(object):
    def specialGrid(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        def copy(l, r1, c1, r2, c2):
            for i in xrange(l):
                for j in xrange(l):
                    result[r2+i][c2+j] = result[r1+i][c1+j]+l*l
        
        total = 1<<n
        result = [[0]*total for _ in xrange(total)]
        l = 1
        for i in xrange(n):
            r, c = 0, total-l
            for dr, dc in ((l, 0), (0, -l), (-l, 0)):
                nr, nc = r+dr, c+dc
                copy(l, r, c, nr, nc)
                r, c = nr, nc
            l <<= 1
        return result