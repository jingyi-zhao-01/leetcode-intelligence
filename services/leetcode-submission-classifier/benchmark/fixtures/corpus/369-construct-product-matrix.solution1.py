# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: construct-product-matrix
# source_path: LeetCode-Solutions-master/Python/construct-product-matrix.py
# solution_class: Solution
# submission_id: c507daa27b3bc638f9c90592417643f5cbcf4369
# seed: 380445470

# Time:  O(m * n)
# Space: O(m * n)

# prefix sum

class Solution(object):
    def constructProductMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        MOD = 12345
        right = [1]*(len(grid)*len(grid[0])+1)
        for i in reversed(xrange(len(grid))):
            for j in reversed(xrange(len(grid[0]))):
                right[i*len(grid[0])+j] = (right[(i*len(grid[0])+j)+1]*grid[i][j])%MOD
        left = 1
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                grid[i][j], left = (left*right[(i*len(grid[0])+j)+1])%MOD, (left*grid[i][j])%MOD
        return grid