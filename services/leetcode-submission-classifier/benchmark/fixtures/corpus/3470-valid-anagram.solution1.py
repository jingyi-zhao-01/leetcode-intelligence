# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: valid-anagram
# source_path: LeetCode-Solutions-master/Python/valid-anagram.py
# solution_class: Solution
# submission_id: 3bba81febfd5504d5bd7eb3d10e109583b8962b3
# seed: 4142723

# Time:  O(n)
# Space: O(1)

import collections

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        count = collections.defaultdict(int)
        for c in s:
            count[c] += 1
        for c in t:
            count[c] -= 1
            if count[c] < 0:
                return False
        return True