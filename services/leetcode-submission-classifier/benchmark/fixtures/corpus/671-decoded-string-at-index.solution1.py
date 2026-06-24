# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: decoded-string-at-index
# source_path: LeetCode-Solutions-master/Python/decoded-string-at-index.py
# solution_class: Solution
# submission_id: 538c5be7cc70ce232888ed4e0a980913149af088
# seed: 924121018

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def decodeAtIndex(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        i = 0
        for c in S:
            if c.isdigit():
                i *= int(c)
            else:
                i += 1

        for c in reversed(S):
            K %= i
            if K == 0 and c.isalpha():
                return c

            if c.isdigit():
                i /= int(c)
            else:
                i -= 1