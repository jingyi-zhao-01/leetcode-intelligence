# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: cyclically-rotating-a-grid
# source_path: LeetCode-Solutions-master/Python/cyclically-rotating-a-grid.py
# solution_class: Solution2
# submission_id: a4cedcaab2e2cea7d8d28bc12a2c23ffe496d95e
# seed: 253375994

# Time:  O(m * n)
# Space: O(1)

import fractions


# inplace rotation

class Solution2(object):
    def rotateGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        def get_index(m, n, l):
            if l < m-1:
                return l, 0
            if l < (m-1)+(n-1):
                return m-1, l-(m-1)
            if l < (m-1)+(n-1)+(m-1):
                return (m-1)-(l-((m-1)+(n-1))), n-1
            return 0, (n-1)-(l-((m-1)+(n-1)+(m-1)))

        def reverse(grid, m, n, i, left, right):
            while left < right:
                lr, lc = get_index(m, n, left)
                rr, rc = get_index(m, n, right)
                grid[i+lr][i+lc], grid[i+rr][i+rc] = grid[i+rr][i+rc], grid[i+lr][i+lc]
                left += 1
                right -= 1

        m, n = len(grid), len(grid[0])
        for i in xrange(min(m, n)//2):
            total = 2*((m-1)+(n-1))
            nk = k%total
            reverse(grid, m, n, i, 0, total-1)
            reverse(grid, m, n, i, 0, nk-1)
            reverse(grid, m, n, i, nk, total-1)
            m, n = m-2, n-2
        return grid