# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-generations-to-target-point
# source_path: LeetCode-Solutions-master/Python/minimum-generations-to-target-point.py
# solution_class: Solution2
# submission_id: e56dcf900c58b69d80f67d4b997dfaa6689d0401
# seed: 2979569155

# Time:  O(7^6)
# Space: O(7^3)

# bfs

class Solution2(object):
    def minGenerations(self, points, target):
        """
        :type points: List[List[int]]
        :type target: List[int]
        :rtype: int
        """
        def encode(p):
            return p[0]*7*7+p[1]*7+p[2]
    
        lookup = [False]*(7**3)
        for p in points:
            if lookup[encode(p)]:
                continue
            lookup[encode(p)] = True
        i = k = 0
        while i < len(points):
            if lookup[encode(target)]:
                return k
            total = len(points)
            while i < total:
                for j in xrange(i):
                    p = [(points[i][0]+points[j][0])//2, (points[i][1]+points[j][1])//2, (points[i][2]+points[j][2])//2]
                    if lookup[encode(p)]:
                        continue
                    lookup[encode(p)] = True
                    points.append(p)
                i += 1
            k += 1
        return -1