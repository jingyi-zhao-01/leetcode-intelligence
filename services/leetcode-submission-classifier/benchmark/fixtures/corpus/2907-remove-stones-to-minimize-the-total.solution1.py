# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: remove-stones-to-minimize-the-total
# source_path: LeetCode-Solutions-master/Python/remove-stones-to-minimize-the-total.py
# solution_class: Solution
# submission_id: 41c9c427c9c693ad440e9f35f82971fc0c61293f
# seed: 3152209858

# Time:  O(n + klogn)
# Space: O(1)

import heapq

class Solution(object):
    def minStoneSum(self, piles, k):
        """
        :type piles: List[int]
        :type k: int
        :rtype: int
        """
        for i, x in enumerate(piles):
            piles[i] = -x
        heapq.heapify(piles)
        for i in xrange(k):
            heapq.heappush(piles, heapq.heappop(piles)//2)
        return -sum(piles)