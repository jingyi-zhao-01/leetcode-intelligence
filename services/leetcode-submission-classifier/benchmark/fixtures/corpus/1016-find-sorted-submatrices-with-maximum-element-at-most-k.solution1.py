# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-sorted-submatrices-with-maximum-element-at-most-k
# source_path: LeetCode-Solutions-master/Python/find-sorted-submatrices-with-maximum-element-at-most-k.py
# solution_class: Solution
# submission_id: 2d97558345ad3a6f295a5074a1c81977dd1cc052
# seed: 3060330083

# Time:  O(m * n)
# Space: O(m)

# mono stack

class Solution(object):
    def countSubmatrices(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        def count(heights):
            result = curr = 0
            stk = []
            for i in xrange(len(heights)):
                while stk and heights[stk[-1]] >= heights[i]:
                    j = stk.pop()
                    curr -= (heights[j]-heights[i])*(j-(stk[-1] if stk else -1))
                stk.append(i)
                curr += heights[i]
                result += curr
            return result

        result = 0
        heights = [0]*len(grid)
        for j in reversed(range(len(grid[0]))):
            for i in xrange(len(grid)):
                heights[i] = 0 if grid[i][j] > k else heights[i]+1 if j+1 < len(grid[0]) and grid[i][j] >= grid[i][j+1] else 1
            result += count(heights)
        return result