# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-average-pass-ratio
# source_path: LeetCode-Solutions-master/Python/maximum-average-pass-ratio.py
# solution_class: Solution
# submission_id: 7b56f1f9ee2eb4da90765fee9b54e1ba333462d4
# seed: 1670583307

# Time:  O(n + mlogn)
# Space: O(n)

import heapq

class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        """
        :type classes: List[List[int]]
        :type extraStudents: int
        :rtype: float
        """
        def profit(a, b):
            return float(a+1)/(b+1)-float(a)/b

        max_heap = [(-profit(a, b), a, b) for a, b in classes]
        heapq.heapify(max_heap)
        while extraStudents:
            v, a, b = heapq.heappop(max_heap)
            a, b = a+1, b+1
            heapq.heappush(max_heap, (-profit(a, b), a, b))
            extraStudents -= 1
        return sum(float(a)/b for v, a, b in max_heap)/len(classes)