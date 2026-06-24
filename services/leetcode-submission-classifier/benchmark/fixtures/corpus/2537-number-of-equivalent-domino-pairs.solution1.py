# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-equivalent-domino-pairs
# source_path: LeetCode-Solutions-master/Python/number-of-equivalent-domino-pairs.py
# solution_class: Solution
# submission_id: e2df3e455c3ca088eac6e986867c25a5e1bb0e7c
# seed: 4075119967

# Time:  O(n)
# Space: O(n)

import collections

class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        counter = collections.Counter((min(x), max(x)) for x in dominoes)
        return sum(v*(v-1)//2 for v in counter.itervalues())