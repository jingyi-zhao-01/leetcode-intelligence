# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-number-of-flips-to-make-binary-grid-palindromic-i
# source_path: LeetCode-Solutions-master/Python/minimum-number-of-flips-to-make-binary-grid-palindromic-i.py
# solution_class: Solution
# submission_id: e26ab5683df3496d40026e8584fa2c1eda712a22
# seed: 337701118

# Time:  O(m * n)
# Space: O(1)

# array, greedy

class Solution(object):
    def minFlips(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def count(m, n, get):
            return sum(get(i, j) != get(i, ~j) for i in xrange(m) for j in xrange(n//2))

        m, n = len(grid), len(grid[0])
        return min(count(m, n, lambda i, j: grid[i][j]),
                   count(n, m, lambda i, j: grid[j][i]))