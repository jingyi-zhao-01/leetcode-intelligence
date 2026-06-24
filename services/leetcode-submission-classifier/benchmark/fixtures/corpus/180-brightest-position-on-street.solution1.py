# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: brightest-position-on-street
# source_path: LeetCode-Solutions-master/Python/brightest-position-on-street.py
# solution_class: Solution
# submission_id: eaef2841c9219d1c5f89b5b7d7b8e500f3834c38
# seed: 3082793443

# Time:  O(nlogn)
# Space: O(n)

import collections

class Solution(object):
    def brightestPosition(self, lights):
        """
        :type lights: List[List[int]]
        :rtype: int
        """
        count = collections.Counter()
        for i, r in lights:
            count[i-r] += 1
            count[i+r+1] -= 1
        result = None
        max_cnt = cnt = 0
        for i, c in sorted(count.iteritems()):
            cnt += c
            if cnt > max_cnt:
                max_cnt, result = cnt, i
        return result