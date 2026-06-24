# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: remove-letter-to-equalize-frequency
# source_path: LeetCode-Solutions-master/Python/remove-letter-to-equalize-frequency.py
# solution_class: Solution
# submission_id: 8e52fa948b8bb27ab4f17a48429da364f9db067d
# seed: 653105327

# Time:  O(n)
# Space: O(1)

import collections


# freq table, edge cases

class Solution(object):
    def equalFrequency(self, word):
        """
        :type word: str
        :rtype: bool
        """
        cnt = collections.Counter(collections.Counter(word).itervalues())
        if len(cnt) > 2:
            return False
        if len(cnt) == 1:
            a = cnt.keys()[0]
            return a == 1 or cnt[a] == 1
        a, b = cnt.keys()
        if a > b:
            a, b = b, a
        return (a == 1 and cnt[a] == 1) or (a+1 == b and cnt[b] == 1)