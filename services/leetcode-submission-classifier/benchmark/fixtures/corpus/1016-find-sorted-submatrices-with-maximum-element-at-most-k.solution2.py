# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-sorted-submatrices-with-maximum-element-at-most-k
# source_path: LeetCode-Solutions-master/Python/find-sorted-submatrices-with-maximum-element-at-most-k.py
# solution_class: Solution2
# submission_id: 8cf4b67cf13540cdd412873167a2c60624546965
# seed: 2246362141

# Time:  O(m * n)
# Space: O(m)

# mono stack

class Solution2(object):
    def countSubmatrices(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        def count(heights):
            dp, stk = [0]*len(heights), []
            for i in xrange(len(heights)):
                while stk and heights[stk[-1]] >= heights[i]:
                    stk.pop()
                dp[i] = dp[stk[-1]] + heights[i]*(i-stk[-1]) if stk else heights[i]*(i-(-1))
                stk.append(i)
            return sum(dp)

        result = 0
        heights = [0]*len(grid)
        for j in reversed(range(len(grid[0]))):
            for i in xrange(len(grid)):
                heights[i] = 0 if grid[i][j] > k else heights[i]+1 if j+1 < len(grid[0]) and grid[i][j] >= grid[i][j+1] else 1
            result += count(heights)
        return result