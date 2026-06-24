# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-servers-that-handled-most-number-of-requests
# source_path: LeetCode-Solutions-master/Python/find-servers-that-handled-most-number-of-requests.py
# solution_class: Solution
# submission_id: 87108ce083ebaba1ef3cae8bc1c636a95d86969e
# seed: 4230891802

# Time:  O(nlogk)
# Space: O(k)

import itertools
import heapq

class Solution(object):
    def busiestServers(self, k, arrival, load):
        """
        :type k: int
        :type arrival: List[int]
        :type load: List[int]
        :rtype: List[int]
        """
        count = [0]*k
        min_heap_of_endtimes = []
        min_heap_of_nodes_after_curr = []
        min_heap_of_nodes_before_curr = range(k)
        for i, (t, l) in enumerate(itertools.izip(arrival, load)):
            if i % k == 0:
                min_heap_of_nodes_before_curr, min_heap_of_nodes_after_curr = [], min_heap_of_nodes_before_curr
            while min_heap_of_endtimes and min_heap_of_endtimes[0][0] <= t:
                _, free = heapq.heappop(min_heap_of_endtimes)
                if free < i % k:
                    heapq.heappush(min_heap_of_nodes_before_curr, free)
                else:
                    heapq.heappush(min_heap_of_nodes_after_curr, free)
            min_heap_of_candidates = min_heap_of_nodes_after_curr if min_heap_of_nodes_after_curr else min_heap_of_nodes_before_curr
            if not min_heap_of_candidates:
                continue
            node = heapq.heappop(min_heap_of_candidates)
            count[node] += 1
            heapq.heappush(min_heap_of_endtimes, (t+l, node))
        max_count = max(count)
        return [i for i in xrange(k) if count[i] == max_count]