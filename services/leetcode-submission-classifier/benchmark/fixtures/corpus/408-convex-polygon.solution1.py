# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: convex-polygon
# source_path: LeetCode-Solutions-master/Python/convex-polygon.py
# solution_class: Solution
# submission_id: 6c6946818f3c3c2a172579466164b96464528a66
# seed: 2043343261

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def isConvex(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        def det(A):
            return A[0][0]*A[1][1] - A[0][1]*A[1][0]

        n, prev, curr = len(points), 0, None
        for i in xrange(len(points)):
            A = [[points[(i+j) % n][0] - points[i][0], points[(i+j) % n][1] - points[i][1]] for j in (1, 2)]
            curr = det(A)
            if curr:
                if curr * prev < 0:
                    return False
                prev = curr
        return True