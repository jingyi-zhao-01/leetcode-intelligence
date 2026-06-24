# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: distant-barcodes
# source_path: LeetCode-Solutions-master/Python/distant-barcodes.py
# solution_class: Solution
# submission_id: 568059d9fc185f57199470376ff6d386684104a5
# seed: 953592167

# Time:  O(n), k is the number of distinct barcodes
# Space: O(k)

import collections
import itertools

class Solution(object):
    def rearrangeBarcodes(self, barcodes):
        """
        :type barcodes: List[int]
        :rtype: List[int]
        """
        k = 2
        cnts = collections.Counter(barcodes)
        bucket_cnt = max(cnts.itervalues())
        result = [0]*len(barcodes)
        i = (len(barcodes)-1)%k
        for c in itertools.chain((c for c, v in cnts.iteritems() if v == bucket_cnt), (c for c, v in cnts.iteritems() if v != bucket_cnt)):
            for _ in xrange(cnts[c]):
                result[i] = c
                i += k
                if i >= len(result):
                    i = (i-1)%k
        return result