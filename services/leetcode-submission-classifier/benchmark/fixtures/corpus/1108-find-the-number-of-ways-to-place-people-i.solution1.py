# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-number-of-ways-to-place-people-i
# source_path: LeetCode-Solutions-master/Python/find-the-number-of-ways-to-place-people-i.py
# solution_class: Solution
# submission_id: 02e79bc13901181268ae8bc8e5a83345d5e8c3e7
# seed: 1297543849

# Time:  O(n^2)
# Space: O(1)

# sort, array

class Solution(object):
    def numberOfPairs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key=lambda x: (x[0], -x[1]))
        result = 0
        for i in xrange(len(points)):
            y = float("-inf")
            for j in xrange(i+1, len(points)):
                if points[i][1] < points[j][1]:
                    continue
                if points[j][1] > y:
                    y = points[j][1]
                    result += 1
        return result