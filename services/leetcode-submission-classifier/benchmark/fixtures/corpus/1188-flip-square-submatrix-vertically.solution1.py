# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: flip-square-submatrix-vertically
# source_path: LeetCode-Solutions-master/Python/flip-square-submatrix-vertically.py
# solution_class: Solution
# submission_id: ce9682172bd67969530eeb4408e84eafb12db0d1
# seed: 2870033330

# Time:  O(k^2)
# Space: O(1)

# array

class Solution(object):
    def reverseSubmatrix(self, grid, x, y, k):
        """
        :type grid: List[List[int]]
        :type x: int
        :type y: int
        :type k: int
        :rtype: List[List[int]]
        """
        for i in xrange(k//2):
            for j in xrange(k):
                grid[x+i][y+j], grid[x+(k-1-i)][y+j] = grid[x+(k-1-i)][y+j], grid[x+i][y+j]
        return grid