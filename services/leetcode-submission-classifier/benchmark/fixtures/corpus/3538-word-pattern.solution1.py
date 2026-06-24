# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: word-pattern
# source_path: LeetCode-Solutions-master/Python/word-pattern.py
# solution_class: Solution
# submission_id: 11964e0ffc73f76ebc27d8b0a9dc63c87f447d69
# seed: 2674351899

# Time:  O(n)
# Space: O(c), c is unique count of pattern

from itertools import izip  # Generator version of zip.

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if len(pattern) != self.wordCount(str):
            return False

        w2p, p2w = {}, {}
        for p, w in izip(pattern, self.wordGenerator(str)):
            if w not in w2p and p not in p2w:
                # Build mapping. Space: O(c)
                w2p[w] = p
                p2w[p] = w
            elif w not in w2p or w2p[w] != p:
                # Contradict mapping.
                return False
        return True

    def wordCount(self, str):
        cnt = 1 if str else 0
        for c in str:
            if c == ' ':
                cnt += 1
        return cnt

    # Generate a word at a time without saving all the words.
    def wordGenerator(self, str):
        w = ""
        for c in str:
            if c == ' ':
                yield w
                w = ""
            else:
                w += c
        yield w