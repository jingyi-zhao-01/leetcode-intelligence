# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximize-sum-of-at-most-k-distinct-elements
# source_path: LeetCode-Solutions-master/Python/maximize-sum-of-at-most-k-distinct-elements.py
# solution_class: Solution2
# submission_id: fccfb2c38c7e6d33fe07f5b9fd24511f3efeb770
# seed: 3125984317

# Time:  O(nlogk)
# Space: O(k)

import heapq


# heap, sort

class Solution2(object):
    def maxKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        min_heap = []
        for x in set(nums):
            heapq.heappush(min_heap, x)
            if len(min_heap) == k+1:
                heapq.heappop(min_heap)
        result = []
        while min_heap:
            result.append(heapq.heappop(min_heap))
        result.reverse()
        return result