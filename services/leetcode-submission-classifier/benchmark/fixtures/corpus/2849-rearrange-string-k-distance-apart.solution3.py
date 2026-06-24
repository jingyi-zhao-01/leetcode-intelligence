# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: rearrange-string-k-distance-apart
# source_path: LeetCode-Solutions-master/Python/rearrange-string-k-distance-apart.py
# solution_class: Solution3
# submission_id: 1236d1c12ac09ef353506e6e197d3282237ae19a
# seed: 3369804215

# Time:  O(n)
# Space: O(c)

import collections
import itertools

class Solution3(object):
    def rearrangeString(self, s, k):
        """
        :type str: str
        :type k: int
        :rtype: str
        """
        cnts = collections.Counter(s)
        bucket_cnt = max(cnts.itervalues())
        buckets = [[] for _ in xrange(bucket_cnt)]
        i = 0
        for c in itertools.chain((c for c, v in cnts.iteritems() if v == bucket_cnt),
                                 (c for c, v in cnts.iteritems() if v == bucket_cnt-1),
                                 (c for c, v in cnts.iteritems() if v <= bucket_cnt-2)):
            for _ in xrange(cnts[c]):
                buckets[i].append(c)
                i = (i+1) % max(cnts[c], bucket_cnt-1)
        if any(len(buckets[i]) < k for i in xrange(len(buckets)-1)):
            return ""
        return "".join(map(lambda x : "".join(x), buckets))