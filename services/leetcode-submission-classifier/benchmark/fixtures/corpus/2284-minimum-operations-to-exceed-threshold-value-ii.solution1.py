# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-operations-to-exceed-threshold-value-ii
# source_path: LeetCode-Solutions-master/Python/minimum-operations-to-exceed-threshold-value-ii.py
# solution_class: Solution
# submission_id: f28f55324f8aecd6982e8627c7a9e0e5ce35d925
# seed: 193598737

# Time:  O(nlogn)
# Space: O(n)

import heapq


# simulation, heap

class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = 0
        heapq.heapify(nums)
        while nums:
            if nums[0] >= k:
                break
            mn1 = heapq.heappop(nums)
            mn2 = heapq.heappop(nums)
            heapq.heappush(nums, 2*mn1+mn2)
            result += 1
        return result