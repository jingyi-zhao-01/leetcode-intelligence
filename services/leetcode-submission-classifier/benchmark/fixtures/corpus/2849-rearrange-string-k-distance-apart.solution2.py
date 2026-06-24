# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: rearrange-string-k-distance-apart
# source_path: LeetCode-Solutions-master/Python/rearrange-string-k-distance-apart.py
# solution_class: Solution2
# submission_id: 75ca4bd3dc1640a04742dbd0aade790ab75647a0
# seed: 188416999

# Time:  O(n)
# Space: O(c)

import collections
import itertools

class Solution2(object):
    def rearrangeString(self, s, k):
        """
        :type str: str
        :type k: int
        :rtype: str
        """
        if not k:
            return s
        cnts = collections.Counter(s)
        bucket_cnt = (len(s)+k-1)//k
        if not (max(cnts.itervalues()) <= bucket_cnt and cnts.values().count(bucket_cnt) <= (len(s)-1)%k+1):
            return ""
        result = [0]*len(s)
        i = 0
        for c in itertools.chain((c for c, v in cnts.iteritems() if v == bucket_cnt),
                                 (c for c, v in cnts.iteritems() if v <= bucket_cnt-2),
                                 (c for c, v in cnts.iteritems() if v == bucket_cnt-1)):
            for _ in xrange(cnts[c]):
                result[i] = c
                i += k
                if i >= len(result):
                    i = i%k+1
        return "".join(result)