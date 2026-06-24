# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: best-position-for-a-service-centre
# source_path: LeetCode-Solutions-master/Python/best-position-for-a-service-centre.py
# solution_class: Solution2
# submission_id: c161008a1be869f3b2f94e7f79bd4edbe33eaf67
# seed: 1996585987

# Time:  O(n * iter), iter is the number of iterations
# Space: O(1)

# see reference:
# - https://en.wikipedia.org/wiki/Geometric_median
# - https://wikimedia.org/api/rest_v1/media/math/render/svg/b3fb215363358f12687100710caff0e86cd9d26b
# Weiszfeld's algorithm

class Solution2(object):
    def getMinDistSum(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: float
        """
        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        EPS = 1e-6
        def dist(positions, p):
            return sum(((p[0]-x)**2 + (p[1]-y)**2)**0.5 for x, y in positions)
        
        median = [0.0, 0.0]
        median[0] = float(sum(x for x, _ in positions))/len(positions)
        median[1] = float(sum(y for _, y in positions))/len(positions)
        result = dist(positions, median)
        delta = float(max(max(positions, key=lambda x: x[0])[0],
                          max(positions, key=lambda x: x[1])[1])) - \
                float(min(min(positions, key=lambda x: x[0])[0],
                          min(positions, key=lambda x: x[1])[1]))
        while delta > EPS:
            for dx, dy in DIRECTIONS:
                new_median = [median[0] + delta*dx, median[1] + delta*dy]
                nd = dist(positions, new_median)
                if nd < result: 
                    result = nd 
                    median = new_median
                    break 
            else:
                delta /= 2.0
        return result 