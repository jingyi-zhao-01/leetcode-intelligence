# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: substrings-that-begin-and-end-with-the-same-letter
# source_path: LeetCode-Solutions-master/Python/substrings-that-begin-and-end-with-the-same-letter.py
# solution_class: Solution
# submission_id: be12f9a54ffc384512f599d15990aee22997f2e0
# seed: 33269361

# Time:  O(n)
# Space: O(1)

import collections

class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        cnt = collections.Counter()
        for c in s:
            cnt[c] += 1
            result += cnt[c]
        return result