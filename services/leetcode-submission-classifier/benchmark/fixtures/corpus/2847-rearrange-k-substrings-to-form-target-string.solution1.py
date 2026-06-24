# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: rearrange-k-substrings-to-form-target-string
# source_path: LeetCode-Solutions-master/Python/rearrange-k-substrings-to-form-target-string.py
# solution_class: Solution
# submission_id: d6ce77056ec65d71b9e7ba53ce00121cac073d59
# seed: 1444749843

# Time:  O(n)
# Space: O(n)

import collections


# freq table

class Solution(object):
    def isPossibleToRearrange(self, s, t, k):
        """
        :type s: str
        :type t: str
        :type k: int
        :rtype: bool
        """
        cnt = collections.defaultdict(int)
        l = len(s)//k
        for i in xrange(0, len(s), l):
            cnt[s[i:i+l]] += 1
            cnt[t[i:i+l]] -= 1
        return all(v == 0 for v in cnt.itervalues())