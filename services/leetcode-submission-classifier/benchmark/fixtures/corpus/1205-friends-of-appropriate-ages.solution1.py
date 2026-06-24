# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: friends-of-appropriate-ages
# source_path: LeetCode-Solutions-master/Python/friends-of-appropriate-ages.py
# solution_class: Solution
# submission_id: 7ea97b9322743449a63075395ba681800b1ea3a3
# seed: 1993779124

# Time:  O(a^2 + n), a is the number of ages,
#                    n is the number of people
# Space: O(a)

import collections

class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        def request(a, b):
            return 0.5*a+7 < b <= a

        c = collections.Counter(ages)
        return sum(int(request(a, b)) * c[a]*(c[b]-int(a == b))
                   for a in c
                   for b in c)