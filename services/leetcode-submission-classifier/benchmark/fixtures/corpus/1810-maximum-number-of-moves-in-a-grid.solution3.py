# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-number-of-moves-in-a-grid
# source_path: LeetCode-Solutions-master/Python/maximum-number-of-moves-in-a-grid.py
# solution_class: Solution3
# submission_id: 88c34e33d31f0cb0f86531c299269ebdc1471111
# seed: 322329200

# Time:  O(m * n)
# Space: O(m)

# dp

class Solution3(object):
    def maxMoves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        q = set(xrange(len(grid)))
        for c in xrange(len(grid[0])-1):
            new_q = set()
            for r in q:
                if grid[r][c] < grid[r][c+1]:
                    new_q.add(r)
                if r-1 >= 0 and grid[r][c] < grid[r-1][c+1]:
                    new_q.add(r-1)
                if r+1 < len(grid) and grid[r][c] < grid[r+1][c+1]:
                    new_q.add(r+1)
            q = new_q
            if not q:
                break
        else:
            c = len(grid[0])-1
        return c