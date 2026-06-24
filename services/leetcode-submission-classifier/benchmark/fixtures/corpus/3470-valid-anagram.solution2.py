# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: valid-anagram
# source_path: LeetCode-Solutions-master/Python/valid-anagram.py
# solution_class: Solution2
# submission_id: 321872095f001be2a7d92d043a26a23edd039447
# seed: 65319151

# Time:  O(n)
# Space: O(1)

import collections

class Solution2(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return collections.Counter(s) == collections.Counter(t)