# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: largest-rectangle-in-histogram
# source_path: LeetCode-Solutions-master/Python/largest-rectangle-in-histogram.py
# solution_class: Solution
# submission_id: 0cb480e34f281f742142e34be950f950df43ae19
# seed: 551562157

# Time:  O(n)
# Space: O(n)

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stk, result = [-1], 0
        for i in xrange(len(heights)+1):
            while stk[-1] != -1 and (i == len(heights) or heights[stk[-1]] >= heights[i]):
                result = max(result, heights[stk.pop()]*((i-1)-stk[-1]))
            stk.append(i) 
        return result