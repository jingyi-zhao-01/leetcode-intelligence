# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: rearrange-string-k-distance-apart
# source_path: LeetCode-Solutions-master/Python/rearrange-string-k-distance-apart.py
# solution_class: Solution
# submission_id: 8103a878ef07f3dab7e85537f4d76a38b61d8de1
# seed: 4192721856

# Time:  O(n)
# Space: O(c)

import collections
import itertools

class Solution(object):
    def rearrangeString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if not k:
            return s
        cnts = collections.Counter(s)
        bucket_cnt = max(cnts.itervalues())
        if not ((bucket_cnt-1)*k+sum(x == bucket_cnt for x in cnts.itervalues()) <= len(s)):
            return ""
        result = [0]*len(s)
        i = (len(s)-1)%k
        for c in itertools.chain((c for c, v in cnts.iteritems() if v == bucket_cnt), (c for c, v in cnts.iteritems() if v != bucket_cnt)):
            for _ in xrange(cnts[c]):
                result[i] = c
                i += k
                if i >= len(result):
                    i = (i-1)%k
        return "".join(result)