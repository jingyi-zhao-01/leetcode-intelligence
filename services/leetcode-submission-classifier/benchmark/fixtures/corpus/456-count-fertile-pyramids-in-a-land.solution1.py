# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-fertile-pyramids-in-a-land
# source_path: LeetCode-Solutions-master/Python/count-fertile-pyramids-in-a-land.py
# solution_class: Solution
# submission_id: 96b4324edc80055c7727a05241bb350e335e1df3
# seed: 79738975

# Time:  O(m * n)
# Space: O(n)

class Solution(object):
    def countPyramids(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def count(grid, reverse):
            def get_grid(i, j):
                return grid[~i][j] if reverse else grid[i][j]

            result = 0
            dp = [0]*len(grid[0])
            for i in xrange(1, len(grid)):
                new_dp = [0]*len(grid[0])
                for j in xrange(1, len(grid[0])-1):
                    if get_grid(i, j) == get_grid(i-1, j-1) == get_grid(i-1, j) == get_grid(i-1, j+1) == 1:
                        new_dp[j] = min(dp[j-1], dp[j+1])+1
                dp = new_dp
                result += sum(dp)
            return result
        
        return count(grid, False) + count(grid, True)