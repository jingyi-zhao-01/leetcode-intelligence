# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: beautiful-pairs
# source_path: LeetCode-Solutions-master/Python/beautiful-pairs.py
# solution_class: Solution3
# submission_id: e9be33feb4dd90462602d8cae4519d379f3ea90e
# seed: 2485805603

# Time:  O(n) on average
# Space: O(n)

import random
import itertools
import math


# random algorithms, variant of closest pair
# reference: https://github.com/jilljenn/tryalgo/blob/master/tryalgo/closest_points.py
random.seed(0)

class Solution3(object):
    def beautifulPair(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        INF = float("inf")
        MAX_NEIGHBOR_COUNT = 8
        def dist(a, b):
            if a > b:
                a, b = b, a
            return [abs(points[a][0]-points[b][0])+abs(points[a][1]-points[b][1]), a, b]

        def merge_sort(left, right):
            if left == right:
                return
            mid = left + (right-left)//2
            x = points[order[mid]][0]  # added
            merge_sort(left, mid)
            merge_sort(mid+1, right)
            r = mid+1
            tmp = []
            for l in xrange(left, mid+1):
                while r <= right and points[order[r]][1] < points[order[l]][1]:  # modified
                    tmp.append(order[r])
                    r += 1
                tmp.append(order[l])
            order[left:left+len(tmp)] = tmp

            # added below
            stripe = [order[i] for i in xrange(left, right+1) if abs(points[order[i]][0]-x) <= result[0]]
            for i in xrange(len(stripe)-1):
                for j in xrange(i+1, len(stripe)):
                    x, y = stripe[i], stripe[j]
                    if points[y][1]-points[x][1] > result[0]:
                        break
                    result[:] = min(result, dist(x, y))
                else:
                    j = len(stripe)
                assert(j-(i+1) <= MAX_NEIGHBOR_COUNT)

        points = [(i, j) for i, j in itertools.izip(nums1, nums2)]
        result = [INF]*3
        lookup = {}
        for i in reversed(xrange(len(points))):
            if points[i] in lookup:
                result = [0, (i, lookup[points[i]])]
            lookup[points[i]] = i
        if result[0] == 0:
            return result[1]
        order = range(len(points))
        order.sort(key=lambda x: points[x][0])
        merge_sort(0, len(points)-1)
        return result[1:]