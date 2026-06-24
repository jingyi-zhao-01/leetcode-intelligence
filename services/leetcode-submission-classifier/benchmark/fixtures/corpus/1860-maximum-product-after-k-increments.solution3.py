# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-product-after-k-increments
# source_path: LeetCode-Solutions-master/Python/maximum-product-after-k-increments.py
# solution_class: Solution3
# submission_id: 44b72cf1434e49d8d860affeeaaab0f6a5a560bc
# seed: 277416552

# Time:  O(nlogn)
# Space: O(1)

# math, sort

class Solution3(object):
    def maximumProduct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        MOD = 10**9+7
        min_heap = nums
        heapq.heapify(min_heap)
        while k:
            heapq.heappush(min_heap, heapq.heappop(min_heap)+1)
            k -= 1
        return reduce(lambda x, y: x*y%MOD, min_heap)