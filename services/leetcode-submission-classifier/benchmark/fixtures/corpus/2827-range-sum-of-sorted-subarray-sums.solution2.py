# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: range-sum-of-sorted-subarray-sums
# source_path: LeetCode-Solutions-master/Python/range-sum-of-sorted-subarray-sums.py
# solution_class: Solution2
# submission_id: 7a0ffe42f9bb4d48590249ced8c2140c91268520
# seed: 3999886910

# Time:  O(nlog(sum(nums)))
# Space: O(n)

# binary search + sliding window solution

class Solution2(object):
    def rangeSum(self, nums, n, left, right):
        """
        :type nums: List[int]
        :type n: int
        :type left: int
        :type right: int
        :rtype: int
        """
        MOD = 10**9+7
        min_heap = []
        for i, num in enumerate(nums, 1):
            heapq.heappush(min_heap, (num, i))
        result = 0
        for i in xrange(1, right+1):
            total, j = heapq.heappop(min_heap)
            if i >= left:
                result = (result+total)%MOD
            if j+1 <= n:
                heapq.heappush(min_heap, (total+nums[j], j+1))
        return result