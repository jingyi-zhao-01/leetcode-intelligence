# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: rearrange-string-k-distance-apart
# source_path: LeetCode-Solutions-master/Python/rearrange-string-k-distance-apart.py
# solution_class: Solution4
# submission_id: 68f2a893a55315f5bebb3bc75253037de76b2f7a
# seed: 531703281

# Time:  O(n)
# Space: O(c)

import collections
import itertools

class Solution4(object):
    def rearrangeString(self, s, k):
        """
        :type str: str
        :type k: int
        :rtype: str
        """
        if k <= 1:
            return s

        cnts = Counter(s)
        heap = []
        for c, cnt in cnts.iteritems():
            heappush(heap, [-cnt, c])

        result = []
        while heap:
            used_cnt_chars = []
            for _ in xrange(min(k, len(s) - len(result))):
                if not heap:
                    return ""
                cnt_char = heappop(heap)
                result.append(cnt_char[1])
                cnt_char[0] += 1
                if cnt_char[0] < 0:
                    used_cnt_chars.append(cnt_char)
            for cnt_char in used_cnt_chars:
                heappush(heap, cnt_char)

        return "".join(result)