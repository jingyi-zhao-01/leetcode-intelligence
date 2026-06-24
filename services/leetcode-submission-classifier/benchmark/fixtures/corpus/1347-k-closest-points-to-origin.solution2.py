# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: k-closest-points-to-origin
# source_path: LeetCode-Solutions-master/Python/k-closest-points-to-origin.py
# solution_class: Solution2
# submission_id: de3939d0dc828adf548dbe4594bc11b77a67d5fb
# seed: 2190857110

# Time:  O(n) on average
# Space: O(1)

# quick select solution
from random import randint

class Solution2(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        def dist(point):
            return point[0]**2 + point[1]**2
        
        max_heap = []
        for point in points:
            heapq.heappush(max_heap, (-dist(point), point))
            if len(max_heap) > K:
                heapq.heappop(max_heap)
        return [heapq.heappop(max_heap)[1] for _ in xrange(len(max_heap))]