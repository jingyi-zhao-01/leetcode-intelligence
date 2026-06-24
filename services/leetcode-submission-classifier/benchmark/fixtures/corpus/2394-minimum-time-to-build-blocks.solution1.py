# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-time-to-build-blocks
# source_path: LeetCode-Solutions-master/Python/minimum-time-to-build-blocks.py
# solution_class: Solution
# submission_id: 91b95ab0bffdb4cf0bb8afd20cc7fd47d9046b89
# seed: 3383426321

# Time:  O(nlogn)
# Space: O(n)

import heapq

class Solution(object):
    def minBuildTime(self, blocks, split):
        """
        :type blocks: List[int]
        :type split: int
        :rtype: int
        """
        heapq.heapify(blocks)
        while len(blocks) != 1:
            x, y = heapq.heappop(blocks), heapq.heappop(blocks)
            heapq.heappush(blocks, y+split)
        return heapq.heappop(blocks)