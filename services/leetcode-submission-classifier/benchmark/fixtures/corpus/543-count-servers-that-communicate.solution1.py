# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-servers-that-communicate
# source_path: LeetCode-Solutions-master/Python/count-servers-that-communicate.py
# solution_class: Solution
# submission_id: bd9c6c4faa64f63a3b326924b8af3ba3a3acf00a
# seed: 2428747582

# Time:  O(m * n)
# Space: O(m + n)

class Solution(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = [0]*len(grid), [0]*len(grid[0])
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j]:
                    rows[i] += 1
                    cols[j] += 1
        result = 0
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j] and (rows[i] > 1 or cols[j] > 1):
                    result += 1
        return result