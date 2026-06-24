# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-area-rectangle-with-point-constraints-i
# source_path: LeetCode-Solutions-master/Python/maximum-area-rectangle-with-point-constraints-i.py
# solution_class: Solution2
# submission_id: 295e5bfdae686962afbfadbb1e0b9aa919879b20
# seed: 3207071207

# Time:  O(nlogn)
# Space: O(n)

# sort, fenwick tree, hash table

class Solution2(object):
    def maxRectangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        result = -1
        points.sort()
        for i in xrange(len(points)-3):
            if points[i][0] != points[i+1][0]:
                continue
            j = next((j for j in xrange(i+2, len(points)-1) if points[i][1] <= points[j][1] <= points[i+1][1]), len(points)-1)
            if j == len(points)-1 or not (points[j][0] == points[j+1][0] and points[i][1] == points[j][1] and points[i+1][1] == points[j+1][1]):
                continue
            result = max(result, (points[i+1][1]-points[i][1])*(points[j][0]-points[i][0]))
        return result