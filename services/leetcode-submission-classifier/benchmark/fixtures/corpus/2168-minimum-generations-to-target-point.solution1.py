# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-generations-to-target-point
# source_path: LeetCode-Solutions-master/Python/minimum-generations-to-target-point.py
# solution_class: Solution
# submission_id: 28a80520113458680db5c12cdf2edc7b522a98ca
# seed: 256685338

# Time:  O(7^6)
# Space: O(7^3)

# bfs

class Solution(object):
    def minGenerations(self, points, target):
        """
        :type points: List[List[int]]
        :type target: List[int]
        :rtype: int
        """
        def encode(p):
            return p[0]*7*7+p[1]*7+p[2]
    
        lookup = [False]*(7**3)
        k = total = 0
        for p in points:
            if lookup[encode(p)]:
                continue
            if p == target:
                return k
            lookup[encode(p)] = True
        i = 0
        while i < len(points):
            if i == total:
                total = len(points)
                k += 1
            for j in xrange(i):
                p = [(points[i][0]+points[j][0])//2, (points[i][1]+points[j][1])//2, (points[i][2]+points[j][2])//2]
                if lookup[encode(p)]:
                    continue
                if p == target:
                    return k
                lookup[encode(p)] = True
                points.append(p)
            i += 1
        return -1