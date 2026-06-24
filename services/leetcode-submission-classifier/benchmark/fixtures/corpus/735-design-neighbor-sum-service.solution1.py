# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: design-neighbor-sum-service
# source_path: LeetCode-Solutions-master/Python/design-neighbor-sum-service.py
# solution_class: Solution
# submission_id: 7d94fba51e87cd50063217c74d854b5e75dc3ad9
# seed: 1603507988

# Time:  ctor:        O(n^2)
#        adjacentSum: O(1)
#.       diagonalSum: O(1)
# Space: O(n^2)

# hash table
class neighborSum(object):
    ADJACENTS = ((1, 0), (0, 1), (-1, 0), (0, -1))
    DIAGONALS = ((1, 1), (1, -1), (-1, 1), (-1, -1))


    def __init__(self, grid):
        """
        :type grid: List[List[int]]
        """
        self.__grid = grid
        self.__lookup = [None]*(len(grid)*len(grid[0]))
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                self.__lookup[grid[i][j]] = (i, j)


    def adjacentSum(self, value):
        """
        :type value: int
        :rtype: int
        """
        return self.__sum(value, neighborSum.ADJACENTS)
    

    def diagonalSum(self, value):
        """
        :type value: int
        :rtype: int
        """
        return self.__sum(value, neighborSum.DIAGONALS)


    def __sum(self, value, directions):
        i, j = self.__lookup[value]
        total = 0
        for di, dj in directions:
            ni, nj = i+di, j+dj
            if not (0 <= ni < len(self.__grid) and 0 <= nj < len(self.__grid[0])):
                continue
            total += self.__grid[ni][nj]
        return total

