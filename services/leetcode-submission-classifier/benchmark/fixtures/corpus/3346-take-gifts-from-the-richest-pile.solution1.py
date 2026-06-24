# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: take-gifts-from-the-richest-pile
# source_path: LeetCode-Solutions-master/Python/take-gifts-from-the-richest-pile.py
# solution_class: Solution
# submission_id: ccd311be7d0203613a4308a8b15dcbbdc1a61be8
# seed: 1546139531

# Time:  O(n + klogn)
# Space: O(1)

import heapq


# heap

class Solution(object):
    def pickGifts(self, gifts, k):
        """
        :type gifts: List[int]
        :type k: int
        :rtype: int
        """
        for i, x in enumerate(gifts):
            gifts[i] = -x
        heapq.heapify(gifts)
        for _ in xrange(k):
            x = heapq.heappop(gifts)
            heapq.heappush(gifts, -int((-x)**0.5))
        return -sum(gifts)