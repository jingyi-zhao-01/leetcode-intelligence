# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-servers-that-handled-most-number-of-requests
# source_path: LeetCode-Solutions-master/Python/find-servers-that-handled-most-number-of-requests.py
# solution_class: Solution2
# submission_id: 3c3f44180992fbe885ccb2f6d377c37f01a009d4
# seed: 1778040239

# Time:  O(nlogk)
# Space: O(k)

import itertools
import heapq

class Solution2(object):
    def busiestServers(self, k, arrival, load):
        """
        :type k: int
        :type arrival: List[int]
        :type load: List[int]
        :rtype: List[int]
        """
        count = [0]*k 
        min_heap_of_endtimes = []
        availables = sortedcontainers.SortedList(xrange(k))  # O(klogk)
        for i, (t, l) in enumerate(itertools.izip(arrival, load)):
            while min_heap_of_endtimes and min_heap_of_endtimes[0][0] <= t:
                _, free = heapq.heappop(min_heap_of_endtimes)  # O(logk)
                availables.add(free)  # O(logk)
            if not availables: 
                continue
            idx = availables.bisect_left(i % k) % len(availables)  # O(logk)
            node = availables.pop(idx)  # O(logk)
            count[node] += 1
            heapq.heappush(min_heap_of_endtimes, (t+l, node))  # O(logk)
        max_count = max(count)
        return [i for i in xrange(k) if count[i] == max_count]