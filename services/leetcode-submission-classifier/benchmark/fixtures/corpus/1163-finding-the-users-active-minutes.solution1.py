# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: finding-the-users-active-minutes
# source_path: LeetCode-Solutions-master/Python/finding-the-users-active-minutes.py
# solution_class: Solution
# submission_id: 6fc827c0def31f7af65b68187466014e27436ef0
# seed: 799049035

# Time:  O(n)
# Space: O(n)

import collections

class Solution(object):
    def findingUsersActiveMinutes(self, logs, k):
        """
        :type logs: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        lookup = collections.defaultdict(set)
        for u, t in logs:
            lookup[u].add(t)
        result = [0]*k
        for _, ts in lookup.iteritems():
            result[len(ts)-1] += 1
        return result