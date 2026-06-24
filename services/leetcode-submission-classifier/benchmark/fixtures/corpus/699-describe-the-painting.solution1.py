# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: describe-the-painting
# source_path: LeetCode-Solutions-master/Python/describe-the-painting.py
# solution_class: Solution
# submission_id: 55b449f642a535ab0a1fe2f690a1206d1e600ff9
# seed: 619264648

# Time:  O(nlogn)
# Space: O(n)

import collections

class Solution(object):
    def splitPainting(self, segments):
        """
        :type segments: List[List[int]]
        :rtype: List[List[int]]
        """
        counts = collections.defaultdict(int)
        for s, e, c in segments:
            counts[s] += c
            counts[e] -= c
        points = sorted(x for x in counts.iteritems())

        result = []
        overlap = prev = 0
        for curr, cnt in points:
            if overlap:
                result.append([prev, curr, overlap])
            overlap += cnt
            prev = curr
        return result