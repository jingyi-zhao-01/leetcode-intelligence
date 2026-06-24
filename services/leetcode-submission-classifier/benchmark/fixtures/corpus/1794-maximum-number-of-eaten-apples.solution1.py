# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-number-of-eaten-apples
# source_path: LeetCode-Solutions-master/Python/maximum-number-of-eaten-apples.py
# solution_class: Solution
# submission_id: 10469a2e7b2ab4559766628c10957ec9ed2d5f4c
# seed: 1239701318

# Time:  O(nlogn)
# Space: O(n)

import heapq

class Solution(object):
    def eatenApples(self, apples, days):
        """
        :type apples: List[int]
        :type days: List[int]
        :rtype: int
        """
        min_heap = []
        result = i = 0
        while i < len(apples) or min_heap:
            if i < len(apples) and apples[i] > 0:
                heapq.heappush(min_heap, [i+days[i], i])
            while min_heap and (min_heap[0][0] <= i or apples[min_heap[0][1]] == 0):
                heapq.heappop(min_heap)
            if min_heap:
                apples[min_heap[0][1]] -= 1
                result += 1
            i += 1
        return result