# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-submatrices-with-equal-frequency-of-x-and-y
# source_path: LeetCode-Solutions-master/Python/count-submatrices-with-equal-frequency-of-x-and-y.py
# solution_class: Solution
# submission_id: 4366e2411389ad83cc31581d694c34c392c88af1
# seed: 4001159541

# Time:  O(n * m)
# Space: O(n * m)

# dp

class Solution(object):
    def numberOfSubmatrices(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        result = 0
        dp1 = [[0]*(len(grid[0])+1) for _ in xrange(len(grid)+1)]
        dp2 = [[0]*(len(grid[0])+1) for _ in xrange(len(grid)+1)]
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                dp1[i+1][j+1] = dp1[i][j+1]+dp1[i+1][j]-dp1[i][j]+int(grid[i][j] == 'X')
                dp2[i+1][j+1] = dp2[i][j+1]+dp2[i+1][j]-dp2[i][j]+int(grid[i][j] == 'Y')
                result += int(dp1[i+1][j+1] == dp2[i+1][j+1] != 0)
        return result