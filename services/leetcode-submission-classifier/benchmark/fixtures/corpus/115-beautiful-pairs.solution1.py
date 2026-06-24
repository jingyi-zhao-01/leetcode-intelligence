# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: beautiful-pairs
# source_path: LeetCode-Solutions-master/Python/beautiful-pairs.py
# solution_class: Solution
# submission_id: 4f310354a1e3e4bb0bad7535d98bf64d5532cc5b
# seed: 1873665661

# Time:  O(n) on average
# Space: O(n)

import random
import itertools
import math


# random algorithms, variant of closest pair
# reference: https://github.com/jilljenn/tryalgo/blob/master/tryalgo/closest_points.py
random.seed(0)

class Solution(object):
    def beautifulPair(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        INF = float("inf")
        def dist(a, b):
            if a[2] > b[2]:
                a, b = b, a
            return [abs(a[0]-b[0])+abs(a[1]-b[1]), a[2], b[2]]

        def cell(point, size):
            x, y, _ = point
            return math.floor(x/size), math.floor(y/size)

        def improve():
            lookup = {}
            for p in points:
                i, j = map(int, cell(p, result[0]/2.0))
                for ni in xrange(i-2, (i+2)+1):
                    for nj in xrange(j-2, (j+2)+1):
                        if (ni, nj) not in lookup:
                            continue
                        d = dist(p, lookup[ni, nj])
                        if d < result:
                            result[:] = d
                            return True
                lookup[i, j] = p
            return False

        points = [(i, j, idx) for idx, (i, j) in enumerate(itertools.izip(nums1, nums2))]
        result = [INF]*3
        lookup = {}
        for i in reversed(xrange(len(points))):
            if points[i][:2] in lookup:
                result = [0, i, lookup[points[i][:2]]]
            lookup[points[i][:2]] = i
        if result[0] == 0:
            return result[1:]
        random.shuffle(points)
        result = dist(points[0], points[1])
        while improve():
            pass
        return result[1:]