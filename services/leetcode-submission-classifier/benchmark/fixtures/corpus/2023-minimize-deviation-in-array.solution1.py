# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimize-deviation-in-array
# source_path: LeetCode-Solutions-master/Python/minimize-deviation-in-array.py
# solution_class: Solution
# submission_id: fc889f565289df860cfaab3ca34792579df14408
# seed: 2678711401

# Time:  O((n * log(max_num)) * logn)
# Space: O(n)

import heapq

class Solution(object):
    def minimumDeviation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_heap = [-num*2 if num%2 else -num for num in nums]
        heapq.heapify(max_heap)
        min_elem = -max(max_heap)
        result = float("inf")
        while len(max_heap) == len(nums):
            num = -heapq.heappop(max_heap)
            result = min(result, num-min_elem)
            if not num%2:
                min_elem = min(min_elem, num//2)
                heapq.heappush(max_heap, -num//2)
        return result