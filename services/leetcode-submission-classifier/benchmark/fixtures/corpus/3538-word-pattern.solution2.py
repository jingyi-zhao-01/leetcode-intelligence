# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: word-pattern
# source_path: LeetCode-Solutions-master/Python/word-pattern.py
# solution_class: Solution2
# submission_id: da91724fb16a649a2c74c9d06bfc2e17cb539a4c
# seed: 4278320114

# Time:  O(n)
# Space: O(c), c is unique count of pattern

from itertools import izip  # Generator version of zip.

class Solution2(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split()  # Space: O(n)
        if len(pattern) != len(words):
            return False

        w2p, p2w = {}, {}
        for p, w in izip(pattern, words):
            if w not in w2p and p not in p2w:
                # Build mapping. Space: O(c)
                w2p[w] = p
                p2w[p] = w
            elif w not in w2p or w2p[w] != p:
                # Contradict mapping.
                return False
        return True