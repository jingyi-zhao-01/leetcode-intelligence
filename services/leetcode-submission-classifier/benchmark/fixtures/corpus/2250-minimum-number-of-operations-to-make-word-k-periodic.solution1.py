# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-number-of-operations-to-make-word-k-periodic
# source_path: LeetCode-Solutions-master/Python/minimum-number-of-operations-to-make-word-k-periodic.py
# solution_class: Solution
# submission_id: 90654bd23d2381b01582eb2bbe3fccb5ec6fbd53
# seed: 959731536

# Time:  O(n)
# Space: O(n)

import collections


# freq table

class Solution(object):
    def minimumOperationsToMakeKPeriodic(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        cnt = collections.Counter(word[i:i+k]for i in xrange(0, len(word), k))
        return len(word)//k-max(cnt.itervalues())