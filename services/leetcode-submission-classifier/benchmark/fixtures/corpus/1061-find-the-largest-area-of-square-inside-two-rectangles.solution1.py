# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-largest-area-of-square-inside-two-rectangles
# source_path: LeetCode-Solutions-master/Python/find-the-largest-area-of-square-inside-two-rectangles.py
# solution_class: Solution
# submission_id: 9f170a83a6ad6e3b639f69ad34a28ab7c92a76bb
# seed: 2483381240

# Time:  O(n^2)
# Space: O(1)

# brute force, math

class Solution(object):
    def largestSquareArea(self, bottomLeft, topRight):
        """
        :type bottomLeft: List[List[int]]
        :type topRight: List[List[int]]
        :rtype: int
        """
        result = 0
        for i in xrange(len(bottomLeft)):
            for j in xrange(i+1, len(bottomLeft)):
                max_x = max(bottomLeft[i][0], bottomLeft[j][0])
                min_x = min(topRight[i][0], topRight[j][0])
                max_y = max(bottomLeft[i][1], bottomLeft[j][1])
                min_y = min(topRight[i][1], topRight[j][1])
                result = max(result, min(min_x-max_x, min_y-max_y))
        return result**2