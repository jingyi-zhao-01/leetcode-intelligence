# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: custom-sort-string
# source_path: LeetCode-Solutions-master/Python/custom-sort-string.py
# solution_class: Solution
# submission_id: f231c3c09809d528ede7b9addbe20e909892ad0d
# seed: 1320769782

# Time:  O(n)
# Space: O(1)

import collections

class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        counter, s = collections.Counter(T), set(S)
        result = [c*counter[c] for c in S]
        result.extend([c*counter for c, counter in counter.iteritems() if c not in s])
        return "".join(result)