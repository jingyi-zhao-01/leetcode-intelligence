# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: using-a-robot-to-print-the-lexicographically-smallest-string
# source_path: LeetCode-Solutions-master/Python/using-a-robot-to-print-the-lexicographically-smallest-string.py
# solution_class: Solution
# submission_id: ec722a37cf330b9f7eeca5c49992f886deda5044
# seed: 2208154705

# Time:  O(n)
# Space: O(n)

import collections


# freq table, greedy

class Solution(object):
    def robotWithString(self, s):
        """
        :type s: str
        :rtype: str
        """
        cnt = collections.Counter(s)
        result, stk = [], []
        mn = 'a'
        for c in s:
            stk.append(c)
            cnt[c] -= 1
            while mn < 'z' and cnt[mn] == 0:
                mn = chr(ord(mn)+1)
            while stk and stk[-1] <= mn:
                result.append(stk.pop())
        return "".join(result) 