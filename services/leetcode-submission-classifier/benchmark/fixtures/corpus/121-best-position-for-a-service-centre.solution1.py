# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: best-position-for-a-service-centre
# source_path: LeetCode-Solutions-master/Python/best-position-for-a-service-centre.py
# solution_class: Solution
# submission_id: 15330724926b544e4055b3318c95c9f16633afdb
# seed: 1591936291

# Time:  O(n * iter), iter is the number of iterations
# Space: O(1)

# see reference:
# - https://en.wikipedia.org/wiki/Geometric_median
# - https://wikimedia.org/api/rest_v1/media/math/render/svg/b3fb215363358f12687100710caff0e86cd9d26b
# Weiszfeld's algorithm

class Solution(object):
    def getMinDistSum(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: float
        """
        EPS = 1e-6
        def norm(p1, p2):
            return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5
        
        def geometry_median(positions, median):
            numerator, denominator = [0.0, 0.0], 0.0
            for p in positions:
                l = norm(median, p)
                if not l:
                    continue                       
                numerator[0] += p[0]/l
                numerator[1] += p[1]/l
                denominator += 1/l
            if denominator == 0.0:
                return True, None
            return False, [numerator[0]/denominator, numerator[1]/denominator]

        median = [float(sum(p[0] for p in positions))/len(positions),
                  float(sum(p[1] for p in positions))/len(positions)]
        prev_median = [float("-inf"), float("-inf")]
        while norm(median, prev_median)*len(positions) > EPS:
            stopped, new_median = geometry_median(positions, median)
            if stopped:
                break
            median, prev_median = new_median, median
        return sum(norm(median, p) for p in positions)