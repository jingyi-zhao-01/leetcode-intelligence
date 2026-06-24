# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-elegance-of-a-k-length-subsequence
# source_path: LeetCode-Solutions-master/Python/maximum-elegance-of-a-k-length-subsequence.py
# solution_class: Solution
# submission_id: cb9697ad84ed80e7af223d006359da8f4a6da0e2
# seed: 967296307

# Time:  O(nlogk)
# Space: O(k)

import heapq
from sortedcontainers import SortedList


# heap, sorted list, greedy

class Solution(object):
    def findMaximumElegance(self, items, k):
        """
        :type items: List[List[int]]
        :type k: int
        :rtype: int
        """
        curr = 0
        lookup = set()
        stk = []
        for p, c in heapq.nlargest(k, items):
            if c in lookup:
                stk.append(p)
            curr += p
            lookup.add(c)
        sl = SortedList()
        lookup2 = {}
        for p, c in items:
            if c in lookup:
                continue
            if c in lookup2:
                if lookup2[c] >= p:
                    continue
                sl.remove((lookup2[c], c))
            sl.add((p, c))
            lookup2[c] = p
            if len(sl) > len(stk):
                del lookup2[sl[0][1]]
                del sl[0]
        result = curr+len(lookup)**2
        for p, c in reversed(sl):
            curr += p-stk.pop()
            lookup.add(c)
            result = max(result, curr+len(lookup)**2) 
        return result