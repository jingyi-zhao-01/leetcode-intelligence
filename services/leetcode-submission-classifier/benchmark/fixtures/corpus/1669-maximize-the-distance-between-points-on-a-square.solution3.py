# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximize-the-distance-between-points-on-a-square
# source_path: LeetCode-Solutions-master/Python/maximize-the-distance-between-points-on-a-square.py
# solution_class: Solution3
# submission_id: 91d11f49072150789efaace43972791a69b11099
# seed: 3980362650

# Time:  O(nlogn + nlogs), s = side
# Space: O(n)

# sort, binary search, greedy, two pointers, sliding window

class Solution3(object):
    def maxDistance(self, side, points, k):
        """
        :type side: int
        :type points: List[List[int]]
        :type k: int
        :rtype: int
        """
        def binary_search_right(left, right, check):
            while left <= right:
                mid = left + (right-left)//2
                if not check(mid):
                    right = mid-1
                else:
                    left = mid+1
            return right

        def check(i, d):
            j = i
            for _ in xrange(k-1):
                j = bisect.bisect_left(p, p[j]+d, lo=j+1)
                if j == len(p):
                    return False
            return (p[i]+4*side)-p[j] >= d

        p = []
        for x, y in points:
            if x == 0:
                p.append(0*side+y)
            elif y == side:
                p.append(1*side+x)
            elif x == side:
                p.append(2*side+(side-y))
            else:
                p.append(3*side+(side-x))
        p.sort()
        result = 1
        for i in xrange(len(p)-k+1):
            if p[-1]-p[i] <= result*(k-1):  # to speed up
                break
            result = binary_search_right(result+1, 4*side//k, lambda x: check(i, x))
        return result