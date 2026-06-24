# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: divide-an-array-into-subarrays-with-minimum-cost-ii
# source_path: LeetCode-Solutions-master/Python/divide-an-array-into-subarrays-with-minimum-cost-ii.py
# solution_class: Solution
# submission_id: 763bd0e4a25403e502054ae38e5b3e7f6134b7af
# seed: 2440526333

# Time:  O(nlogd)
# Space: O(d)

import heapq


# sliding window, heap

class Solution(object):
    def minimumCost(self, nums, k, dist):
        """
        :type nums: List[int]
        :type k: int
        :type dist: int
        :rtype: int
        """
        def get_top(heap, total):
            while abs(heap[0][1]) < i-(1+dist):
                heapq.heappop(heap)
                total[0] -= 1
            return heap[0]
            
        def lazy_delete(heap, total):
            total[0] += 1
            if total[0] <= len(heap)-total[0]:
                return
            heap[:] = [x for x in heap if abs(x[1]) > i-(1+dist)]
            heapq.heapify(heap)
            total[0] = 0

        max_heap, min_heap = [], []
        total1, total2 = [0], [0]
        mn, curr = float("inf"), 0
        for i in xrange(1, len(nums)):
            heapq.heappush(max_heap, (-nums[i], i))
            curr += nums[i]
            if i > k-1:
                x, idx = get_top(max_heap, total1)
                heapq.heappop(max_heap)
                curr -= -x
                heapq.heappush(min_heap, (-x, -idx))
            if i > 1+dist:
                x, idx = get_top(min_heap, total2)
                if (x, idx) <= (nums[i-(1+dist)], -(i-(1+dist))):
                    lazy_delete(min_heap, total2)
                else:
                    lazy_delete(max_heap, total1)
                    heapq.heappop(min_heap)
                    curr -= nums[i-(1+dist)]-x
                    heapq.heappush(max_heap, (-x, -idx))
            if i >= k-1:
                mn = min(mn, curr)
        return nums[0]+mn