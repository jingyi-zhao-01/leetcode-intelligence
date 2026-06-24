# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: max-value-of-equation
# source_path: LeetCode-Solutions-master/Python/max-value-of-equation.py
# solution_class: Solution
# submission_id: 764bf33a327ad6c8a16f3bf68f0efb3ebb6136e2
# seed: 3388011771

# Time:  O(n)
# Space: O(n)

import collections

class Solution(object):
    def findMaxValueOfEquation(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: int
        """
        result = float("-inf")
        dq = collections.deque()
        for i, (x, y) in enumerate(points):
            while dq and points[dq[0]][0] < x-k:
                dq.popleft()
            if dq:
                result = max(result, (points[dq[0]][1]-points[dq[0]][0])+y+x)
            while dq and points[dq[-1]][1]-points[dq[-1]][0] <= y-x:
                dq.pop()
            dq.append(i)
        return result