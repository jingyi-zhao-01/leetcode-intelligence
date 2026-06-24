# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: construct-product-matrix
# source_path: LeetCode-Solutions-master/Python/construct-product-matrix.py
# solution_class: Solution2
# submission_id: 3c9526cf569674e1ad967690ef2626216cc8bd25
# seed: 4155006853

# Time:  O(m * n)
# Space: O(m * n)

# prefix sum

class Solution2(object):
    def constructProductMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        MOD = 12345
        left = [1]*(len(grid)*len(grid[0])+1)
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                left[(i*len(grid[0])+j)+1] = (left[i*len(grid[0])+j]*grid[i][j])%MOD
        right = [1]*(len(grid)*len(grid[0])+1)
        for i in reversed(xrange(len(grid))):
            for j in reversed(xrange(len(grid[0]))):
                right[i*len(grid[0])+j] = (right[(i*len(grid[0])+j)+1]*grid[i][j])%MOD
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                grid[i][j] = (left[i*len(grid[0])+j]*right[(i*len(grid[0])+j)+1])%MOD
        return grid