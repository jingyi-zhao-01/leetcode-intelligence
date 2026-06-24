# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-number-of-pushes-to-type-word-ii
# source_path: LeetCode-Solutions-master/Python/minimum-number-of-pushes-to-type-word-ii.py
# solution_class: Solution
# submission_id: 756495ce6c9e2a12736f2dc30680bb44a664d46c
# seed: 359373033

# Time:  O(n)
# Space: O(26)

import collections


# freq table, greedy

class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        return sum(x*(i//(9-2+1)+1) for i, x in enumerate(sorted(collections.Counter(word).itervalues(), reverse=True)))