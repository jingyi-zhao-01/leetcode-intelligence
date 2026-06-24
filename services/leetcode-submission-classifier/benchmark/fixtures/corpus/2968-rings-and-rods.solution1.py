# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: rings-and-rods
# source_path: LeetCode-Solutions-master/Python/rings-and-rods.py
# solution_class: Solution
# submission_id: 0be010b32dfe8a935f972234fcf124d9abcf267b
# seed: 2100622786

# Time:  O(n)
# Space: O(1)

import collections

class Solution(object):
    def countPoints(self, rings):
        """
        :type rings: str
        :rtype: int
        """
        bits = {'R':0b001, 'G':0b010, 'B':0b100}
        rods = collections.defaultdict(int)
        for i in xrange(0, len(rings), 2):
            rods[int(rings[i+1])] |= bits[rings[i]]
        return sum(x == 0b111 for x in rods.itervalues())