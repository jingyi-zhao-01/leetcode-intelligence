# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: meeting-rooms-iii
# source_path: LeetCode-Solutions-master/Python/meeting-rooms-iii.py
# solution_class: Solution
# submission_id: b0d899220fd858275bee6305b4e936ee1a360e7f
# seed: 289567397

# Time:  O(mlogm + n + mlogn)
# Space: O(n)

import heapq


# one heap solution

class Solution(object):
    def mostBooked(self, n, meetings):
        """
        :type n: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        meetings.sort()
        min_heap = [(meetings[0][0], i) for i in xrange(n)]
        result = [0]*n
        for s, e in meetings:
            while min_heap and min_heap[0][0] < s:
                _, i = heapq.heappop(min_heap)
                heapq.heappush(min_heap, (s, i))
            e2, i = heapq.heappop(min_heap)
            heapq.heappush(min_heap, (e2+(e-s), i))
            result[i] += 1
        return max(xrange(n), key=lambda x:result[x])