# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-a-string-is-an-acronym-of-words
# source_path: LeetCode-Solutions-master/Python/check-if-a-string-is-an-acronym-of-words.py
# solution_class: Solution
# submission_id: 3b9f898f6b5fed1fb852ac9aa1fe57604cc6f602
# seed: 2283113892

# Time:  O(n)
# Space: O(1)

import itertools


# string

class Solution(object):
    def isAcronym(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: bool
        """
        return len(words) == len(s) and all(w[0] == c for w, c in itertools.izip(words, s))