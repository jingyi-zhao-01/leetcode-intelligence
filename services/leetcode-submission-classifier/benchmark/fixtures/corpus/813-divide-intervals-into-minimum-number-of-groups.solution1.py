# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: divide-intervals-into-minimum-number-of-groups
# source_path: LeetCode-Solutions-master/Python/divide-intervals-into-minimum-number-of-groups.py
# solution_class: Solution
# submission_id: 0b7dbfd92c6e9c5c724d6bea78d6b065c7dd1496
# seed: 3319527640

# Time:  O(nlogn)
# Space: O(n)

import collections


# sort, line sweep

class Solution(object):
    def minGroups(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        events = collections.Counter()
        for l, r in intervals:
            events[l] += 1
            events[r+1] -= 1
        result = curr = 0
        for t in sorted(events.iterkeys()):
            curr += events[t]
            result = max(result, curr)
        return result