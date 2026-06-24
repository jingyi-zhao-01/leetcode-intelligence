# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-requests-without-violating-the-limit
# source_path: LeetCode-Solutions-master/Python/maximum-requests-without-violating-the-limit.py
# solution_class: Solution
# submission_id: ae544973bb17d215f6d0fab1fbd1a0fb33a8eb72
# seed: 414167800

# Time:  O(nlogn)
# Space: O(n)

import collections


# hash table, sort, deque, sliding window

class Solution(object):
    def maxRequests(self, requests, k, window):
        """
        :type requests: List[List[int]]
        :type k: int
        :type window: int
        :rtype: int
        """
        lookup = collections.defaultdict(list)
        for u, t in requests:
            lookup[u].append(t)
        result = len(requests)
        for l in lookup.itervalues():
            l.sort()
            dq = collections.deque()
            for x in l:
                dq.append(x)
                if len(dq) <= k:
                    continue
                if dq[-1]-dq[0] > window:
                    dq.popleft()
                    continue
                dq.pop()
                result -= 1                    
        return result