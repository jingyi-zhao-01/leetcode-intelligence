# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-largest-area-of-square-inside-two-rectangles
# source_path: LeetCode-Solutions-master/Python/find-the-largest-area-of-square-inside-two-rectangles.py
# solution_class: Solution2
# submission_id: 3c41137a9435f335191c760ecbdbeb421105397e
# seed: 3558779077

# Time:  O(n^2)
# Space: O(1)

# brute force, math

class Solution2(object):
    def largestSquareArea(self, bottomLeft, topRight):
        """
        :type bottomLeft: List[List[int]]
        :type topRight: List[List[int]]
        :rtype: int
        """
        return max(max(min(min(topRight[i][0], topRight[j][0])-max(bottomLeft[i][0], bottomLeft[j][0]), min(topRight[i][1], topRight[j][1])-max(bottomLeft[i][1], bottomLeft[j][1])) for i in xrange(len(bottomLeft)) for j in xrange(i+1, len(bottomLeft))), 0)**2