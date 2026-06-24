# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-operations-to-write-the-letter-y-on-a-grid
# source_path: LeetCode-Solutions-master/Python/minimum-operations-to-write-the-letter-y-on-a-grid.py
# solution_class: Solution
# submission_id: 01426a3bb2affae322ea79ade50770cb2a39329c
# seed: 3456955689

# Time:  O(n^2)
# Space: O(1)

# array

class Solution(object):
    def minimumOperationsToWriteY(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        cnt = [[0]*3 for _ in xrange(2)]
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                cnt[(i <= (len(grid[0])-1)//2 and (i-j == 0 or i+j == len(grid[0])-1)) or (i > (len(grid[0])-1)//2 == j)][grid[i][j]] += 1
        return len(grid)*len(grid[0])-max(cnt[0][i]+cnt[1][j] for i in xrange(3) for j in xrange(3) if i != j)