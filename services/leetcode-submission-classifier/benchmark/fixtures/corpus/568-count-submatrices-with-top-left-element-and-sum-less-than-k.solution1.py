# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-submatrices-with-top-left-element-and-sum-less-than-k
# source_path: LeetCode-Solutions-master/Python/count-submatrices-with-top-left-element-and-sum-less-than-k.py
# solution_class: Solution
# submission_id: cf5e7e78aa075a70a215f318990654d83ecc1298
# seed: 356487238

# Time:  O(n * m)
# Space: O(1)

# prefix sum

class Solution(object):
    def countSubmatrices(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        result = 0
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if i-1 >= 0:
                    grid[i][j] += grid[i-1][j]
                if j-1 >= 0:
                    grid[i][j] += grid[i][j-1]
                if i-1 >= 0 and j-1 >= 0:
                    grid[i][j] -= grid[i-1][j-1]
                if grid[i][j] <= k:
                    result += 1
        return result