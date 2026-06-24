# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: avoid-flood-in-the-city
# source_path: LeetCode-Solutions-master/Python/avoid-flood-in-the-city.py
# solution_class: Solution
# submission_id: 87f992b75a0d68a002e178daaef86eb98385c92d
# seed: 946031234

# Time:  O(nlogn)
# Space: O(n)

import collections
import heapq

class Solution(object):
    def avoidFlood(self, rains):
        """
        :type rains: List[int]
        :rtype: List[int]
        """
        lookup = collections.defaultdict(list)
        i = len(rains)-1
        for lake in reversed(rains):
            lookup[lake].append(i)
            i -= 1
        result, min_heap = [], []
        for i, lake in enumerate(rains):
            if lake:
                if len(lookup[lake]) >= 2:
                    lookup[lake].pop()
                    heapq.heappush(min_heap, lookup[lake][-1])
                result.append(-1)
            elif min_heap:
                j = heapq.heappop(min_heap)
                if j < i:
                    return []
                result.append(rains[j])
            else:
                result.append(1)
        return result if not min_heap else []