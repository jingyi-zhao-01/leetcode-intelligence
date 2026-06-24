# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: most-frequent-ids
# source_path: LeetCode-Solutions-master/Python/most-frequent-ids.py
# solution_class: Solution
# submission_id: 557dea380d3541d717ac2d69b3b12fe780a0e226
# seed: 2844487592

# Time:  O(nlogn)
# Space: O(n)

import collections
import itertools
import heapq


# heap

class Solution(object):
    def mostFrequentIDs(self, nums, freq):
        """
        :type nums: List[int]
        :type freq: List[int]
        :rtype: List[int]
        """
        result = []
        cnt = collections.Counter()
        max_heap = []
        for x, f in itertools.izip(nums, freq):
            cnt[x] += f
            heapq.heappush(max_heap, (-cnt[x], x))
            while max_heap and -max_heap[0][0] != cnt[max_heap[0][1]]:
                heapq.heappop(max_heap)
            result.append(-max_heap[0][0] if max_heap else 0)
        return result