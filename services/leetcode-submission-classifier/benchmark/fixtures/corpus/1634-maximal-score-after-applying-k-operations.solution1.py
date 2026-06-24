# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximal-score-after-applying-k-operations
# source_path: LeetCode-Solutions-master/Python/maximal-score-after-applying-k-operations.py
# solution_class: Solution
# submission_id: 0567d6b9b8f1884e29201c9c50a9561e417c1507
# seed: 3336635349

# Time:  O(n + klogn)
# Space: O(1)

import heapq


# heap

class Solution(object):
    def maxKelements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def ceil_divide(a, b):
            return (a+b-1)//b
    
        result = 0
        for i, x in enumerate(nums):
            nums[i] = -x
        heapq.heapify(nums)
        for _ in xrange(k):
            if not nums:
                break
            x = -heapq.heappop(nums)
            result += x
            nx = ceil_divide(x, 3)
            if not nx:
                continue
            heapq.heappush(nums, -nx)
        return result