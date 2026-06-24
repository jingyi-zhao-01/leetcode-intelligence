# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-elegance-of-a-k-length-subsequence
# source_path: LeetCode-Solutions-master/Python/maximum-elegance-of-a-k-length-subsequence.py
# solution_class: Solution3
# submission_id: 8188319c5aa7483ee052359c89294965ea8d68f5
# seed: 1161179188

# Time:  O(nlogk)
# Space: O(k)

import heapq
from sortedcontainers import SortedList


# heap, sorted list, greedy

class Solution3(object):
    def findMaximumElegance(self, items, k):
        """
        :type items: List[List[int]]
        :type k: int
        :rtype: int
        """
        items.sort(reverse=True)
        result = curr = 0
        lookup = set()
        stk = []
        for i in xrange(k):
            if items[i][1] in lookup:
                stk.append(items[i][0])
            curr += items[i][0]
            lookup.add(items[i][1])
        result = curr+len(lookup)**2
        for i in xrange(k, len(items)):
            if items[i][1] in lookup:
                continue
            if not stk:
                break
            curr += items[i][0]-stk.pop()
            lookup.add(items[i][1])
            result = max(result, curr+len(lookup)**2)
        return result