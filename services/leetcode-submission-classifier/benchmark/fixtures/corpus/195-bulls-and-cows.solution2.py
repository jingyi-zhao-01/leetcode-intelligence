# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: bulls-and-cows
# source_path: LeetCode-Solutions-master/Python/bulls-and-cows.py
# solution_class: Solution2
# submission_id: 190fd0e6b5e234dcae4dcfe96fca0b0dcd159fb4
# seed: 2624320468

# Time:  O(n)
# Space: O(10) = O(1)

import operator


# One pass solution.
from collections import defaultdict, Counter
from itertools import izip, imap

class Solution2(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        A = sum(imap(operator.eq, secret, guess))
        B = sum((Counter(secret) & Counter(guess)).values()) - A
        return "%dA%dB" % (A, B)