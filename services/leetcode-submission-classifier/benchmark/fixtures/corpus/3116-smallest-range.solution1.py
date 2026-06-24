# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: smallest-range
# source_path: LeetCode-Solutions-master/Python/smallest-range.py
# solution_class: Solution
# submission_id: 86adbe34f5d555df2ca0cb0e17065844c58a56ca
# seed: 4253665467

# Time:  O(nlogk)
# Space: O(k)

import heapq

class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        left, right = float("inf"), float("-inf")
        min_heap = []
        for row in nums:
            left = min(left, row[0])
            right = max(right, row[0])
            it = iter(row)
            heapq.heappush(min_heap, (next(it, None), it))

        result = (left, right)
        while min_heap:
            (val, it) = heapq.heappop(min_heap)
            val = next(it, None)
            if val is None:
                break
            heapq.heappush(min_heap, (val, it))
            left, right = min_heap[0][0], max(right, val)
            if right - left < result[1] - result[0]:
                result = (left, right)
        return result