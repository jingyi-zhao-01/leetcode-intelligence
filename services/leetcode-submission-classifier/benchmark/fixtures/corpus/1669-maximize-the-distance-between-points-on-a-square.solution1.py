# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximize-the-distance-between-points-on-a-square
# source_path: LeetCode-Solutions-master/Python/maximize-the-distance-between-points-on-a-square.py
# solution_class: Solution
# submission_id: 6f50a24aa076cfd8f5af399f1d87476442dd5a08
# seed: 1365603570

# Time:  O(nlogn + nlogs), s = side
# Space: O(n)

# sort, binary search, greedy, two pointers, sliding window

class Solution(object):
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

        def check(d):
            intervals = [(0, 0, 1)]
            i = 0
            for right in xrange(1, len(p)):
                left, cnt = right, 1
                while i < len(intervals):
                    l, r, c = intervals[i]
                    if p[right]-p[r] < d:
                        break
                    if (p[l]+4*side)-p[right] >= d:
                        if c+1 >= cnt:
                            cnt = c+1
                            left = l
                    i += 1
                intervals.append((left, right, cnt))
            return max(x[2] for x in intervals) >= k

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
        return binary_search_right(1, 4*side//k, check)