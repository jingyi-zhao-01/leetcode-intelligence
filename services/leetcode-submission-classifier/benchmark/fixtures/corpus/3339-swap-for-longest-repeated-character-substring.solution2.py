# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: swap-for-longest-repeated-character-substring
# source_path: LeetCode-Solutions-master/Python/swap-for-longest-repeated-character-substring.py
# solution_class: Solution2
# submission_id: 882cf3a8bf7af6de61c92ca1e925f438e9ad3e99
# seed: 3669970877

# Time:  O(n)
# Space: O(1)

import collections

class Solution2(object):
    def maxRepOpt1(self, text):
        """
        :type text: str
        :rtype: int
        """
        A = [[c, len(list(group))] for c, group in itertools.groupby(text)]
        total_count = collections.Counter(text)
        result = max(min(l+1, total_count[c]) for c, l in A)
        for i in xrange(1, len(A)-1):
            if A[i-1][0] == A[i+1][0] and A[i][1] == 1:
                result = max(result, min(A[i-1][1] + 1 + A[i+1][1], total_count[A[i+1][0]]))
        return result