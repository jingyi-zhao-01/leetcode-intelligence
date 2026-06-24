# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: largest-local-values-in-a-matrix
# source_path: LeetCode-Solutions-master/Python/largest-local-values-in-a-matrix.py
# solution_class: Solution
# submission_id: a2da975688792120a17f54b51f3a80e77e7628a3
# seed: 1718793979

# Time:  O(m * n)
# Space: O(1)

# array

class Solution(object):
    def largestLocal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        def find_max(i, j):
            return max(grid[ni][nj] for ni in xrange(i, i+3) for nj in xrange(j, j+3))

        return [[find_max(i, j) for j in xrange(len(grid[0])-2)] for i in xrange(len(grid)-2)]