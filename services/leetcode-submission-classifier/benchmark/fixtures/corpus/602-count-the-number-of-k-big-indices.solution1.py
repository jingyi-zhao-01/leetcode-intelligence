# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-the-number-of-k-big-indices
# source_path: LeetCode-Solutions-master/Python/count-the-number-of-k-big-indices.py
# solution_class: Solution
# submission_id: 0ce715dec11558cce55d583a14f88d2e2a2e691a
# seed: 244762881

# Time:  O(nlogk)
# Space: O(n)

import heapq


# heap

class Solution(object):
    def kBigIndices(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        right = [False]*len(nums)
        max_heap1 = []
        for i in reversed(xrange(len(nums))):
            if len(max_heap1) == k and nums[i] > -max_heap1[0]:
                right[i] = True
            heapq.heappush(max_heap1, -nums[i])
            if len(max_heap1) == k+1:
                heapq.heappop(max_heap1)
        result = 0
        max_heap2 = []
        for i in xrange(len(nums)):
            if len(max_heap2) == k and nums[i] > -max_heap2[0] and right[i]:
                result += 1
            heapq.heappush(max_heap2, -nums[i])
            if len(max_heap2) == k+1:
                heapq.heappop(max_heap2)
        return result