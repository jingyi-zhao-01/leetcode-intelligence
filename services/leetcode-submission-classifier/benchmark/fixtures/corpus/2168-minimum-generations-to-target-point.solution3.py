# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-generations-to-target-point
# source_path: LeetCode-Solutions-master/Python/minimum-generations-to-target-point.py
# solution_class: Solution3
# submission_id: 910a30e63906075a972c14c2cbd02ffcdab3d5d6
# seed: 3689060722

# Time:  O(7^6)
# Space: O(7^3)

# bfs

class Solution3(object):
    def minGenerations(self, points, target):
        """
        :type points: List[List[int]]
        :type target: List[int]
        :rtype: int
        """
        def encode(p):
            return p[0]*7*7+p[1]*7+p[2]
    
        q = []
        lookup = [False]*(7**3)
        for p in points:
            if lookup[encode(p)]:
                continue
            lookup[encode(p)] = True
            q.append(p)
        k = 0
        while q:
            if lookup[encode(target)]:
                return k
            new_q = []
            for i in xrange(len(points)-len(q), len(points)):
                for j in xrange(i):
                    p = [(points[i][0]+points[j][0])//2, (points[i][1]+points[j][1])//2, (points[i][2]+points[j][2])//2]
                    if lookup[encode(p)]:
                        continue
                    lookup[encode(p)] = True
                    new_q.append(p)
            points.extend(new_q)
            q = new_q
            k += 1
        return -1