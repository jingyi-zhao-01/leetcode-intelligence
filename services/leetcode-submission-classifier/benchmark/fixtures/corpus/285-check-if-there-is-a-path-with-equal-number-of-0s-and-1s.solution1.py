# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-there-is-a-path-with-equal-number-of-0s-and-1s
# source_path: LeetCode-Solutions-master/Python/check-if-there-is-a-path-with-equal-number-of-0s-and-1s.py
# solution_class: Solution
# submission_id: 8e8f94a972591f7b42814937237d8676afa35e68
# seed: 3100103096

# Time:  O(m * n)
# Space: O(n)

# dp

class Solution(object):
    def isThereAPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        if (len(grid)+len(grid[0])-1)%2:
            return False
        dp_left = [[float("inf")]*(len(grid[0])+1) for _ in xrange(2)]
        dp_left[0][1] = dp_left[1][0] = 0
        dp_right = [[float("-inf")]*(len(grid[0])+1) for _ in xrange(2)]
        dp_right[0][1] = dp_right[1][0] = 0
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                dp_left[(i+1)%2][j+1] = min(dp_left[i%2][j+1], dp_left[(i+1)%2][j])+grid[i][j]
                dp_right[(i+1)%2][j+1] = max(dp_right[i%2][j+1], dp_right[(i+1)%2][j])+grid[i][j]
        return dp_left[len(grid)%2][-1] <= (len(grid)+len(grid[0])-1)//2 <= dp_right[len(grid)%2][-1]