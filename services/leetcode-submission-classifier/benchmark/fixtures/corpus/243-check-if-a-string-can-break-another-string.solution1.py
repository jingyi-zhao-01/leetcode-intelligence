# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-a-string-can-break-another-string
# source_path: LeetCode-Solutions-master/Python/check-if-a-string-can-break-another-string.py
# solution_class: Solution
# submission_id: 0996ce9243d8711135c858279cbe21928c6d7f10
# seed: 3405298630

# Time:  O(n)
# Space: O(1)

import collections
import string

class Solution(object):
    def checkIfCanBreak(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        def is_break(count1, count2):
            curr1, curr2 = 0, 0
            for c in string.ascii_lowercase:
                curr1 += count1[c]
                curr2 += count2[c]
                if curr1 < curr2:
                    return False
            return True

        count1, count2 = collections.Counter(s1), collections.Counter(s2)
        return is_break(count1, count2) or is_break(count2, count1)