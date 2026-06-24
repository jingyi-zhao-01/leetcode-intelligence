# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximal-score-after-applying-k-operations
# source_path: LeetCode-Solutions-master/Python/maximal-score-after-applying-k-operations.py
# solution_class: Solution2
# submission_id: a95fb0a744fc7fdb9a615ef1f04cbb117a936f2d
# seed: 1834491488

# Time:  O(n + klogn)
# Space: O(1)

import heapq


# heap

class Solution2(object):
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
            x = -heapq.heappop(nums)
            result += x
            heapq.heappush(nums, -ceil_divide(x, 3))
        return result