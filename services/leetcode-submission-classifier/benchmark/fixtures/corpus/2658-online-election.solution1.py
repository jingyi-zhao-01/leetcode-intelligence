# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: online-election
# source_path: LeetCode-Solutions-master/Python/online-election.py
# solution_class: Solution
# submission_id: 6068b15bd76ab117dd1d345acad53446ae079aba
# seed: 269844014

# Time:  ctor: O(n)
#        q:    O(logn)
# Space: O(n)

import collections
import itertools
import bisect


class TopVotedCandidate(object):

    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        lead = -1
        self.__lookup, count = [], collections.defaultdict(int)
        for t, p in itertools.izip(times, persons):
            count[p] += 1
            if count[p] >= count[lead]:
                lead = p
                self.__lookup.append((t, lead))

    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        return self.__lookup[bisect.bisect(self.__lookup,
                                           (t, float("inf")))-1][1]



