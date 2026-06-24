# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: the-number-of-the-smallest-unoccupied-chair
# source_path: LeetCode-Solutions-master/Python/the-number-of-the-smallest-unoccupied-chair.py
# solution_class: Solution
# submission_id: e82254e94d5ca88d5f21b119495cd70b72ccb8f3
# seed: 27040021

# Time:  O(nlogn)
# Space: O(n)

import heapq

class Solution(object):
    def smallestChair(self, times, targetFriend):
        """
        :type times: List[List[int]]
        :type targetFriend: int
        :rtype: int
        """
        events = []
        for i, (s, e) in enumerate(times): 
            events.append((s, True, i))
            events.append((e, False, i))
        events.sort()

        lookup = {}
        min_heap = []
        for _, arrival, i in events: 
            if not arrival: 
                heapq.heappush(min_heap, lookup.pop(i))
                continue
            lookup[i] = heapq.heappop(min_heap) if min_heap else len(lookup)
            if i == targetFriend:
                break
        return lookup[targetFriend]