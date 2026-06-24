# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-window-substring
# source_path: LeetCode-Solutions-master/Python/minimum-window-substring.py
# solution_class: Solution
# submission_id: 976782da1ea57ebb0d0394951c4c7c6d9890afaa
# seed: 2619854706

# Time:  O(n)
# Space: O(k), k is the number of different characters

import collections

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        count, remain = collections.Counter(t), len(t)
        i, left, right = 0, -1, -1
        for j, c in enumerate(s):
            remain -= count[c] > 0
            count[c] -= 1
            if remain:
                continue
            while count[s[i]] < 0:  # greedily discard uneeds
                count[s[i]] += 1
                i += 1
            if right == -1 or j-i+1 < right-left+1:
                left, right = i, j
        return s[left:right+1]