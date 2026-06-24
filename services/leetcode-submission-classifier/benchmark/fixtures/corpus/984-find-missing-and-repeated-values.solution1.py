# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-missing-and-repeated-values
# source_path: LeetCode-Solutions-master/Python/find-missing-and-repeated-values.py
# solution_class: Solution
# submission_id: 044b8ca153b8fb2c04042507b699b5210507f038
# seed: 3383520428

# Time:  O(n^2)
# Space: O(1)

# bit manipulation

class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        n = len(grid)
        a_xor_b = 0
        for i in xrange(n**2):
            r, c = divmod(i, n)
            a_xor_b ^= grid[r][c]^(i+1)
        base = a_xor_b&-a_xor_b
        result = [0]*2
        for i in xrange(n**2):
            r, c = divmod(i, len(grid[0]))
            result[1 if (i+1)&base != 0 else 0] ^= i+1
            result[1 if grid[r][c]&base != 0 else 0] ^= grid[r][c]
        if any(x == result[1] for row in grid for x in row):
            result[0], result[1] = result[1], result[0]
        return result