# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: make-the-prefix-sum-non-negative
# source_path: LeetCode-Solutions-master/Python/make-the-prefix-sum-non-negative.py
# solution_class: Solution
# submission_id: 8ce00abaec1e1fa3912659d069956fae43d54b5a
# seed: 1992307353

# Time:  O(nlogn)
# Space: O(n)

import heapq


# prefix sum, greedy, heap

class Solution(object):
    def makePrefSumNonNegative(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = prefix = 0
        min_heap = []
        for x in nums:
            heapq.heappush(min_heap, x)
            prefix += x
            if prefix < 0:
                prefix -= heapq.heappop(min_heap)
                result += 1
        return result