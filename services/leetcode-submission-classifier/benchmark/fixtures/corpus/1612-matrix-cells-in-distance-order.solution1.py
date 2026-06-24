# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: matrix-cells-in-distance-order
# source_path: LeetCode-Solutions-master/Python/matrix-cells-in-distance-order.py
# solution_class: Solution
# submission_id: da0d89215b5c498668bbd8e3d44c26647c34e54b
# seed: 2443093093

# Time:  O(m * n)
# Space: O(1)

class Solution(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        def append(R, C, r, c, result):
            if 0 <= r < R and 0 <= c < C:
                result.append([r, c])
            
        result = [[r0, c0]]
        for d in xrange(1, R+C):
            append(R, C, r0-d, c0, result)
            for x in xrange(-d+1, d):
                append(R, C, r0+x, c0+abs(x)-d, result)
                append(R, C, r0+x, c0+d-abs(x), result)
            append(R, C, r0+d, c0, result)
        return result