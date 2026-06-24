# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: backspace-string-compare
# source_path: LeetCode-Solutions-master/Python/backspace-string-compare.py
# solution_class: Solution
# submission_id: 2b75d80a89610fedb0bd75e0967a48b20ad99b72
# seed: 1066903686

# Time:  O(m + n)
# Space: O(1)

import itertools

class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def findNextChar(S):
            skip = 0
            for i in reversed(xrange(len(S))):
                if S[i] == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield S[i]

        return all(x == y for x, y in
                   itertools.izip_longest(findNextChar(S), findNextChar(T)))