# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: remove-letter-to-equalize-frequency
# source_path: LeetCode-Solutions-master/Python/remove-letter-to-equalize-frequency.py
# solution_class: Solution2
# submission_id: 14532dc049cb372011d03f737ef15745c39d3fd4
# seed: 3697454781

# Time:  O(n)
# Space: O(1)

import collections


# freq table, edge cases

class Solution2(object):
    def equalFrequency(self, word):
        """
        :type word: str
        :rtype: bool
        """
        cnt = collections.Counter(collections.Counter(word))
        for c in word:
            cnt[c] -= 1
            if len(collections.Counter(c for c in cnt.itervalues() if c)) == 1:
                return True
            cnt[c] += 1
        return False