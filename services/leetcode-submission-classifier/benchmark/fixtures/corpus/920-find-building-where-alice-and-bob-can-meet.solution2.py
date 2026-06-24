# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-building-where-alice-and-bob-can-meet
# source_path: LeetCode-Solutions-master/Python/find-building-where-alice-and-bob-can-meet.py
# solution_class: Solution2
# submission_id: d131e98d9133e42534394dd25d9838209cf75ca3
# seed: 2331741280

# Time:  O(n + qlogn)
# Space: O(n)

# online solution, segment tree, binary search

class Solution2(object):
    def leftmostBuildingQueries(self, heights, queries):
        """
        :type heights: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        result = [-1]*len(queries)
        qs = [[] for _ in xrange(len(heights))]
        for i, (a, b) in enumerate(queries):
            if a > b:
                a, b = b, a
            if a == b or heights[a] < heights[b]:
                result[i] = b
            else:
                qs[b].append((heights[a], i))
        min_heap = []
        for i, h in enumerate(heights):
            for q in qs[i]:
                heapq.heappush(min_heap, q)
            while min_heap and min_heap[0][0] < h:
                _, j = heapq.heappop(min_heap)
                result[j] = i
        return result