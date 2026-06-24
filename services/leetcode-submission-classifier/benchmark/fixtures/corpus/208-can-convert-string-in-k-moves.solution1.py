# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: can-convert-string-in-k-moves
# source_path: LeetCode-Solutions-master/Python/can-convert-string-in-k-moves.py
# solution_class: Solution
# submission_id: 23d85c256b61901a878088b455ba0d367ec67b29
# seed: 2350879745

# Time:  O(n)
# Space: O(1)

import itertools

class Solution(object):
    def canConvertString(self, s, t, k):
        """
        :type s: str
        :type t: str
        :type k: int
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        cnt = [0]*26
        for a, b in itertools.izip(s, t):
            diff = (ord(b)-ord(a)) % len(cnt)
            if diff != 0 and cnt[diff]*len(cnt) + diff > k:
                return False
            cnt[diff] += 1
        return True