# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: distant-barcodes
# source_path: LeetCode-Solutions-master/Python/distant-barcodes.py
# solution_class: Solution2
# submission_id: ab87f74ceece2f9d7ae9625fc735e007aee41f96
# seed: 1185093344

# Time:  O(n), k is the number of distinct barcodes
# Space: O(k)

import collections
import itertools

class Solution2(object):
    def rearrangeBarcodes(self, barcodes):
        """
        :type barcodes: List[int]
        :rtype: List[int]
        """
        cnts = collections.Counter(barcodes)
        sorted_cnts = [[v, k] for k, v in cnts.iteritems()]
        sorted_cnts.sort(reverse=True)

        i = 0
        for v, k in sorted_cnts:
            for _ in xrange(v):
                barcodes[i] = k
                i += 2
                if i >= len(barcodes):
                    i = 1
        return barcodes