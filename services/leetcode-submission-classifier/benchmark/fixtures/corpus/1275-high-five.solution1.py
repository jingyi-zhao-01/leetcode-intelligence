# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: high-five
# source_path: LeetCode-Solutions-master/Python/high-five.py
# solution_class: Solution
# submission_id: 94937faff628a0c13677568f3d802b88dd516be6
# seed: 3815429668

# Time:  O(nlogn)
# Space: O(n)

import collections
import heapq

class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        min_heaps = collections.defaultdict(list)
        for i, val in items:
            heapq.heappush(min_heaps[i], val)
            if len(min_heaps[i]) > 5:
                heapq.heappop(min_heaps[i])
        return [[i, sum(min_heaps[i]) // len(min_heaps[i])] for i in sorted(min_heaps)]