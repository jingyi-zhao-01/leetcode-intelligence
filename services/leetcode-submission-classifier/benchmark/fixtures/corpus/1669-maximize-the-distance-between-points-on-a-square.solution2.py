# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximize-the-distance-between-points-on-a-square
# source_path: LeetCode-Solutions-master/Python/maximize-the-distance-between-points-on-a-square.py
# solution_class: Solution2
# submission_id: f89d77cdea4195f1e6bef3b426536bfbc7cfb7cb
# seed: 3042963173

# Time:  O(nlogn + nlogs), s = side
# Space: O(n)

# sort, binary search, greedy, two pointers, sliding window

class Solution2(object):
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
            for right in xrange(1, len(sorted_points)):
                left, cnt = right, 1
                while i < len(intervals):
                    l, r, c = intervals[i]
                    if abs(sorted_points[right][0]-sorted_points[r][0])+abs(sorted_points[right][1]-sorted_points[r][1]) < d:
                        break
                    if abs(sorted_points[right][0]-sorted_points[l][0])+abs(sorted_points[right][1]-sorted_points[l][1]) >= d:
                        if c+1 >= cnt:
                            cnt = c+1
                            left = l
                    i += 1
                intervals.append((left, right, cnt))
            return max(x[2] for x in intervals) >= k

        p = [[] for _ in xrange(4)]
        for x, y in points:
            if x == 0:
                p[0].append((x, y))
            elif y == side:
                p[1].append((x, y))
            elif x == side:
                p[2].append((x, y))
            else:
                p[3].append((x, y))
        p[0].sort()
        p[1].sort()
        p[2].sort(reverse=True)
        p[3].sort(reverse=True)
        sorted_points = [x for i in xrange(4) for x in p[i]]
        return binary_search_right(1, 4*side//k, check)