# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximal-rectangle
# source_path: LeetCode-Solutions-master/Python/maximal-rectangle.py
# solution_class: Solution
# submission_id: 80a6bcb9841ce5391b17723afa1f524f2a943a8b
# seed: 2656202560

# Time:  O(n^2)
# Space: O(n)

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        def largestRectangleArea(heights):
            stk, result, i = [-1], 0, 0
            for i in xrange(len(heights)+1):
                while stk[-1] != -1 and (i == len(heights) or heights[stk[-1]] >= heights[i]):
                    result = max(result, heights[stk.pop()]*((i-1)-stk[-1]))
                stk.append(i) 
            return result

        if not matrix:
            return 0
        result = 0
        heights = [0]*len(matrix[0])
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[0])):
                heights[j] = heights[j] + 1 if matrix[i][j] == '1' else 0
            result = max(result, largestRectangleArea(heights))
        return result