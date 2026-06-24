# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-building-where-alice-and-bob-can-meet
# source_path: LeetCode-Solutions-master/Python/find-building-where-alice-and-bob-can-meet.py
# solution_class: Solution3
# submission_id: d38fb6eef928374422e98cf320a8d636416fea23
# seed: 3183851089

# Time:  O(n + qlogn)
# Space: O(n)

# online solution, segment tree, binary search

class Solution3(object):
    def leftmostBuildingQueries(self, heights, queries):
        """
        :type heights: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        def binary_search_right(left, right, check):
            while left <= right:
                mid = left + (right-left)//2
                if not check(mid):
                    right = mid-1
                else:
                    left = mid+1
            return right

        result = [-1]*len(queries)
        qs = [[] for _ in xrange(len(heights))]
        for i, (a, b) in enumerate(queries):
            if a > b:
                a, b = b, a
            if a == b or heights[a] < heights[b]:
                result[i] = b
            else:
                qs[b].append((heights[a], i))
        stk = []
        for b in reversed(xrange(len(heights))):
            while stk and stk[-1][0] <= heights[b]:
                stk.pop()
            stk.append((heights[b], b))
            for ha, i in qs[b]:
                j = binary_search_right(0, len(stk)-1, lambda x: stk[x][0] > ha)
                if j >= 0:
                    result[i] = stk[j][1]
        return result