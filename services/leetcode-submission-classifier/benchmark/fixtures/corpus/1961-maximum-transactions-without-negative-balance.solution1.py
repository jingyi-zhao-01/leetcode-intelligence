# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-transactions-without-negative-balance
# source_path: LeetCode-Solutions-master/Python/maximum-transactions-without-negative-balance.py
# solution_class: Solution
# submission_id: 1d12c677bcb40ee8012d8e01643e0a7d3987f67c
# seed: 1334773022

# Time:  O(nlogn)
# Space: O(n)

import heapq


# greedy, heap

class Solution(object):
    def maxTransactions(self, transactions):
        """
        :type transactions: List[int]
        :rtype: int
        """
        min_heap = []
        curr = 0
        for x in transactions:
            heapq.heappush(min_heap, x)
            curr += x
            if curr < 0:
                curr -= heapq.heappop(min_heap)
        return len(min_heap)