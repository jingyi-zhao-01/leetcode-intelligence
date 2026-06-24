# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: beautiful-pairs
# source_path: LeetCode-Solutions-master/Python/beautiful-pairs.py
# solution_class: Solution2
# submission_id: 57180231c455f6dd1c0993bbb0676cfaf4743c11
# seed: 3296557446

# Time:  O(n) on average
# Space: O(n)

import random
import itertools
import math


# random algorithms, variant of closest pair
# reference: https://github.com/jilljenn/tryalgo/blob/master/tryalgo/closest_points.py
random.seed(0)

class Solution2(object):
    def beautifulPair(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        INF = float("inf")
        MAX_NEIGHBOR_COUNT = (8+2)//2
        def dist(a, b):
            if a > b:
                a, b = b, a
            return [abs(points[a][0]-points[b][0])+abs(points[a][1]-points[b][1]), a, b]

        def merge_sort(left, right):
            def update(arr, i):  # added
                for j in reversed(xrange(len(arr))):
                    if points[i][1]-points[arr[j]][1] > result[0]:
                        break
                    result[:] = min(result, dist(i, arr[j]))
                else:
                    j = -1
                assert((len(arr)-1)-j <= MAX_NEIGHBOR_COUNT)

            if left == right:
                return
            mid = left+(right-left)//2
            x = points[order[mid]][0]  # added
            merge_sort(left, mid)
            merge_sort(mid+1, right)
            tmp, tmp_l, tmp_r = [], [], []
            l, r = left, mid+1
            while l <= mid or r <= right:
                if r == right+1 or (l <= mid and points[order[l]][1] <= points[order[r]][1]):  # modified
                    update(tmp_r, order[l])
                    if x-points[order[l]][0] <= result[0]:  # added
                        tmp_l.append(order[l])
                    tmp.append(order[l])
                    l += 1
                else:
                    update(tmp_l, order[r])
                    if points[order[r]][0]-x <= result[0]:  # added
                        tmp_r.append(order[r])
                    tmp.append(order[r])
                    r += 1
            order[left:right+1] = tmp

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