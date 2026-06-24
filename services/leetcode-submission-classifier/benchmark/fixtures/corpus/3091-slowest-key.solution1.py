# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: slowest-key
# source_path: LeetCode-Solutions-master/Python/slowest-key.py
# solution_class: Solution
# submission_id: 1300e835814ce705ab71a7a14f80256888a6d9e6
# seed: 4291001288

# Time:  O(n)
# Space: O(1)

import collections

class Solution(object):
    def slowestKey(self, releaseTimes, keysPressed):
        """
        :type releaseTimes: List[int]
        :type keysPressed: str
        :rtype: str
        """
        result, lookup = 'a', collections.Counter()
        for i, c in enumerate(keysPressed):
            lookup[c] = max(lookup[c], releaseTimes[i]-(releaseTimes[i-1] if i > 0 else 0))
            if lookup[c] > lookup[result] or lookup[c] == lookup[result] and c > result:
                result = c
        return result