# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: queries-on-number-of-points-inside-a-circle
# source_path: LeetCode-Solutions-master/Python/queries-on-number-of-points-inside-a-circle.py
# solution_class: Solution
# submission_id: 1e369f037e8d4d03ab4c0e8eea5131aaeda39172
# seed: 1251558482

# Time:  O(q * n)
# Space: O(1)

class Solution(object):
    def countPoints(self, points, queries):
        """
        :type points: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        result = []
        for i, j, r in queries:
            result.append(0)
            for x, y in points:
                if (x-i)**2+(y-j)**2 <= r**2:
                    result[-1] += 1
        return result