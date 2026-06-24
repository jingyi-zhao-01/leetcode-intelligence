# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-distinct-islands
# source_path: LeetCode-Solutions-master/Python/number-of-distinct-islands.py
# solution_class: Solution
# submission_id: ba93a7d87b04fe0ebea26cf95bf424197d7b8476
# seed: 751575127

# Time:  O(m * n)
# Space: O(m * n)

class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        directions = {'l':[-1,  0], 'r':[ 1,  0], \
                      'u':[ 0,  1], 'd':[ 0, -1]}

        def dfs(i, j, grid, island):
            if not (0 <= i < len(grid) and \
                    0 <= j < len(grid[0]) and \
                    grid[i][j] > 0):
                return False
            grid[i][j] *= -1
            for k, v in directions.iteritems():
                island.append(k)
                dfs(i+v[0], j+v[1], grid, island)
            return True

        islands = set()
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                island = []
                if dfs(i, j, grid, island):
                    islands.add("".join(island))
        return len(islands)