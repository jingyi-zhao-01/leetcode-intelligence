# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-number-of-ways-to-place-people-i
# source_path: LeetCode-Solutions-master/Python/find-the-number-of-ways-to-place-people-i.py
# solution_class: Solution2
# submission_id: 72e455ffceb124f7fa38aeb13a3532bccb3dabc1
# seed: 1077896138

# Time:  O(n^2)
# Space: O(1)

# sort, array

class Solution2(object):
    def numberOfPairs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key=lambda x: (x[0], -x[1]))
        return sum(all(not points[i][1] >= points[k][1] >= points[j][1] for k in xrange(i+1, j))
                   for i in xrange(len(points))
                   for j in xrange(i+1, len(points)) if points[i][1] >= points[j][1])