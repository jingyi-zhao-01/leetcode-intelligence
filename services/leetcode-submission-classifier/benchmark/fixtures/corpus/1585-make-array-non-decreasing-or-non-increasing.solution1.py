# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: make-array-non-decreasing-or-non-increasing
# source_path: LeetCode-Solutions-master/Python/make-array-non-decreasing-or-non-increasing.py
# solution_class: Solution
# submission_id: 36bc2fd34b9c07579fdfd4022c7996d875f542eb
# seed: 945818300

# Time:  O(nlogn)
# Space: O(n)

import heapq


# greedy, heap

class Solution(object):
    def convertArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def f(nums):
            result = 0
            max_heap = []
            for x in nums:
                if max_heap and x < -max_heap[0]:
                    result += -heapq.heappop(max_heap)-x
                    heapq.heappush(max_heap, -x)
                heapq.heappush(max_heap, -x)
            return result
        
        return min(f(nums), f((x for x in reversed(nums))))