# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: amount-of-new-area-painted-each-day
# source_path: LeetCode-Solutions-master/Python/amount-of-new-area-painted-each-day.py
# solution_class: Solution2
# submission_id: 9553aa9242a09fedadf6b402ac04ef56706c9ad7
# seed: 2709627801

# Time:  O(nlogn)
# Space: O(n)

import collections
import heapq


# line sweep, heap

class Solution2(object):
    def amountPainted(self, paint):
        """
        :type paint: List[List[int]]
        :rtype: List[int]
        """
        points = collections.defaultdict(list)
        for i, (s, e) in enumerate(paint):
            points[s].append((True, i))
            points[e].append((False, i))
        sl = SortedList()
        result = [0]*len(paint)
        prev = -1
        for pos in sorted(points.iterkeys()):
            if sl:
                result[sl[0]] += pos-prev
            prev = pos
            for t, i in points[pos]:
                if t:
                    sl.add(i)
                else:
                    sl.remove(i)
        return result